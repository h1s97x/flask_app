# SayHello

*Say hello to the world.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).
>
> 

Demo: http://sayhello.helloflask.com

![Screenshot](https://helloflask.com/screenshots/sayhello.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/sayhello.git
$ cd sayhello
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

## 代码库架构

该代码库是一个基于Flask的Web应用程序，名为"SayHello"。其整体架构可分为以下几个部分：

### 1. 根目录文件

在根目录下，包含了一些配置文件、环境文件、许可证、依赖文件等。这些文件为项目的运行和配置提供了基础支持。

### 2. 应用主体

- ```
  sayhello/
  ```

  ：这是应用的主要部分，包含了应用的所有逻辑和配置。

  - `commands.py`：可能包含了一些自定义的Flask命令。
  - `config.py`：应用的配置信息，如数据库连接、应用密钥等。
  - `errors.py`：定义了应用中的错误处理逻辑。
  - `extensions.py`：初始化并配置Flask应用的扩展，如数据库、邮件等。
  - `forms.py`：定义了应用中的表单类，用于验证用户输入。
  - `models.py`：定义了应用的数据模型，与数据库表对应。
  - `settings.py`：可能包含了一些应用级别的设置或常量。
  - `views.py`：定义了应用的视图函数，处理用户的请求并返回响应。
  - `__init__.py`：初始化应用，并加载配置、扩展和路由。

### 3. 模板和静态文件

- `templates/`：存放HTML模板文件，用于渲染动态页面。
  - `base.html`：基础模板，其他模板可能继承自它。
  - `index.html`：主页模板。
  - `errors/`：存放错误页面的模板，如404和500错误页面。
- `static/`：存放静态文件，如CSS、JS和图片等。这些文件在客户端浏览器中加载和运行，为应用提供样式和交互功能。

### 总结

该代码库是一个结构清晰的Flask Web应用程序，遵循了典型的MVC（模型-视图-控制器）架构模式。其中，`models.py`负责数据模型（M），`views.py`负责处理用户请求并返回响应（C），而`templates/`目录下的HTML文件则负责页面展示（V）。此外，应用还通过`extensions.py`、`forms.py`等文件提供了丰富的功能和验证机制。
