

## Database

大部分程序都需要保存数据，所以不可避免要使用数据库。用来操作数据库的数据库管理系统（DBMS）有很多选择，对于不同类型的程序，不同的使用场景，都会有不同的选择。在这个教程中，我们选择了属于关系型数据库管理系统（RDBMS）的 [SQLite](https://www.sqlite.org/)，它基于文件，不需要单独启动数据库服务器，适合在开发时使用，或是在数据库操作简单、访问量低的程序中使用。

### SQLAlchemy

Flask-SQLAlchemy是一个Flask扩展，它为Flask应用程序提供了一个简单的方式来使用SQLAlchemy进行数据库操作。SQLAlchemy是一个强大的SQL工具包和对象关系映射（ORM）框架，它允许开发者以Python类的形式定义数据库表结构，并通过这些类来操作数据库。
以下是使用Flask-SQLAlchemy连接数据库并进行基本操作的一些步骤：

1. **安装Flask-SQLAlchemy**：
   首先，你需要安装Flask-SQLAlchemy。可以使用pip来安装：

   ```bash
   pip install Flask-SQLAlchemy
   ```

2. **配置数据库URI**：
   在Flask应用中，你需要在配置中指定数据库的URI。URI的格式通常如下：

   ```python
   SQLALCHEMY_DATABASE_URI = '数据库引擎+驱动://用户名:密码@主机地址:端口/数据库名'
   ```

   对于这个变量值，不同的 DBMS 有不同的格式，对于 SQLite 来说，这个值的格式如下：

   ```
   sqlite:////数据库文件的绝对地址
   ```

   ```python
   SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
   ```

3. **初始化SQLAlchemy**：
   在Flask应用中，你需要初始化SQLAlchemy。通常在`app.py`或类似的文件中这样做：

   ```python
   from flask_sqlalchemy import SQLAlchemy
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydatabase.db'
   db = SQLAlchemy(app)
   ```

### 创建数据库模型

在 Watchlist 程序里，目前我们有两类数据要保存：用户信息和电影条目信息。下面分别创建了两个模型类来表示这两张表：

   *app.py：创建数据库模型*

   ```
   class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
       id = db.Column(db.Integer, primary_key=True)  # 主键
       name = db.Column(db.String(20))  # 名字
   
   
   class Movie(db.Model):  # 表名将会是 movie
       id = db.Column(db.Integer, primary_key=True)  # 主键
       title = db.Column(db.String(60))  # 电影标题
       year = db.Column(db.String(4))  # 电影年份
   ```

   模型类的编写有一些限制：

   - 模型类要声明继承 `db.Model`。
   - 每一个类属性（字段）要实例化 `db.Column`，传入的参数为字段的类型，下面的表格列出了常用的字段类。
   - 在 `db.Column()` 中添加额外的选项（参数）可以对字段进行设置。比如，`primary_key` 设置当前字段是否为主键。除此之外，常用的选项还有 `nullable`（布尔值，是否允许为空值）、`index`（布尔值，是否设置索引）、`unique`（布尔值，是否允许重复值）、`default`（设置默认值）等。

   常用的字段类型如下表所示：

   | 字段类           | 说明                                          |
   | :--------------- | :-------------------------------------------- |
   | db.Integer       | 整型                                          |
   | db.String (size) | 字符串，size 为最大长度，比如 `db.String(20)` |
   | db.Text          | 长文本                                        |
   | db.DateTime      | 时间日期，Python `datetime` 对象              |
   | db.Float         | 浮点数                                        |
   | db.Boolean       | 布尔值                                        |

   ### 创建数据库表

模型类创建后，还不能对数据库进行操作，因为我们还没有创建表和数据库文件。下面在 Python Shell 中创建了它们：

   ```
   (env) $ flask shell
   >>> from app import db
   >>> db.create_all()
   ```

打开文件管理器，你会发现项目根目录下出现了新创建的数据库文件 data.db。这个文件不需要提交到 Git 仓库，我们在 .gitignore 文件最后添加一行新规则：

   ```
   *.db
   ```

如果你改动了模型类，想重新生成表模式，那么需要先使用 `db.drop_all()` 删除表，然后重新创建：

   ```
   >>> db.drop_all()
   >>> db.create_all()
   ```

注意这会一并删除所有数据，如果你想在不破坏数据库内的数据的前提下变更表的结构，需要使用数据库迁移工具，比如集成了 [Alembic](https://alembic.sqlalchemy.org/en/latest/) 的 [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) 扩展。

   > **提示** 上面打开 Python Shell 使用的是 `flask shell`命令，而不是 `python`。使用这个命令启动的 Python Shell 激活了“程序上下文”，它包含一些特殊变量，这对于某些操作是必须的（比如上面的 `db.create_all()`调用）。请记住，后续的 Python Shell 都会使用这个命令打开。

   和 `flask shell`类似，我们可以编写一个自定义命令来自动执行创建数据库表操作：

   *app.py：自定义命令 initdb*

   ```
   import click
   
   @app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
   @click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
   def initdb(drop):
       """Initialize the database."""
       if drop:  # 判断是否输入了选项
           db.drop_all()
       db.create_all()
       click.echo('Initialized database.')  # 输出提示信息
   ```

   默认情况下，如果没有指定，函数名称就是命令的名字（注意函数名中的下划线会被转换为连接线），现在执行 `flask initdb` 命令就可以创建数据库表：

   ```
   (env) $ flask initdb
   ```

   使用 `--drop` 选项可以删除表后重新创建：

   ```
   (env) $ flask initdb --drop
   ```

   ### 创建、读取、更新、删除

**创建数据库和表**：
在定义模型后，你需要创建数据库和表。可以使用以下命令：

```bash
flask db init  # 初始化迁移仓库
flask db migrate -m "Initial migration."  # 生成迁移脚本
flask db upgrade  # 应用迁移
```

**进行数据库操作**：
现在你的数据库和表已经创建好了，你可以开始进行增删改查等操作：

- **增加记录**：

  ```python
  new_user = User(username='john', email='john@example.com')
  db.session.add(new_user)
  db.session.commit()
  ```

- **查询记录**：

  ```python
  user = User.query.filter_by(username='john').first()
  ```

- **更新记录**：

  ```python
  user.email = 'newemail@example.com'
  db.session.commit()
  ```

- **删除记录**：

  ```python
  db.session.delete(user)
  db.session.commit()
  ```

**管理数据库会话**：
Flask-SQLAlchemy使用`db.session`来管理数据库会话。所有的数据库操作都需要通过会话来进行，最后调用`commit()`方法来提交会话。
以上是Flask-SQLAlchemy连接数据库并进行基本操作的一个概览。在实际应用中，你可能需要进行更复杂的操作，如关联多个表、处理关系、执行原生SQL查询等，Flask-SQLAlchemy都提供了相应的支持。

