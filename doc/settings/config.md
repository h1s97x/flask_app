## 启动项配置

### host

为了让服务器对外可见，可以在运行 Flask 服务器时使用 `--host` 选项设置为 `0.0.0.0`，这样服务器会监听所有外部请求。

例如，使用命令 `flask run --host=0.0.0.0`。由于个人计算机通常没有公网IP，所以程序只能通过内网IP（如192.168.191.1）在局域网内被访问。局域网内的用户可以通过访问 `http://192.168.191.1:5000` 来看到 "Hello, Flask!" 的消息。

> 若想将程序部署到具有公网IP的服务器上，以供互联网上的任何人访问，可以考虑使用内网穿透/端口转发工具，如ngrok或Localtunnel。

### port

Flask的Web服务器默认监听5000端口，可以通过 `--port` 参数来改变它，比如使用 `flask run --port=8000` 来监听8000端口。此时，程序的主页地址变为 `http://localhost:8000/`。

此外，`flask run` 命令的 `host` 和 `port` 选项也可以通过环境变量 `FLASK_RUN_HOST` 和 `FLASK_RUN_PORT` 来设置。Flask内置命令支持通过环境变量来定义默认选项值，格式为 `FLASK_<COMMAND>_<OPTION>`。可以使用 `flask --help` 命令来查看所有可用的命令。

```
# .flaskenv

FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=9000
```

### config配置

一般一个项目会配置多套环境：开发/测试/生产环境，每套环境的配置不一样，比如不同的运行环境配置的[数据库](https://cloud.tencent.com/solution/database?from_column=20065&from=20065)不一样。

```javascript
import os

class Config(object):
    # DEBUG = False
    JSON_AS_ASCII = False
    # 设置SECRET_KEY
    SECRET_KEY = os.urandom(24)  # 随机字符串

class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/web'
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否显示底层执行的SQL语句
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """生产环境"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@x.x.x.x:3306/web'
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否显示底层执行的SQL语句
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    """测试环境"""
    TESTING = True

# 映射环境对象
config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
```





### Flask 获取配置

Flask 获取配置信息有几种方式，一种是从文件中获取，一种是从定义好的 dict 里获取。

**从文件中获取配置**

从文件里获取提供了几种方式：

```python
app.config.from_object("app.config")

app.config.from_pyfile("./config.py")
```

我们在 app/ 文件夹下创建了一个 config.py 文件，其内容如下：

```python
ABC = "123"
```

在执行完 from_object 或者 from_pyfile 操作之后，可以通过下面的操作获取到这些配置信息：

```python
app.config.get("ABC")
```

**从 dict 中获取配置**

除了从文件中获取，我们还可以使用 from_mapping() 函数，将需要写入的配置放到 dict 里：

```python
app.config.from_mapping({
    "ABC": "123"
})
```

**注意**：我们从文件中或者从 dict 中获取的变量名称都应该是大写的，否则系统不会读入。
