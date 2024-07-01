Flask 有两个主要依赖，一个是 WSGI (Web Server Gateway Interface, Web 服务器网关接 口 ）工具集一Werkzeug(http: //werkzeug.pocoo.org/ ），另 一个是 Jinja2 模板引擎( http: //jinja.pocoo.org/ ） 。
Flask 只保留了 Web 开发的核心功能，其他的功能都由外部扩展来实现，比如数据库成 、 表单认证 、 文件上传等 。





### conda 虚拟环境

导出环境依赖：

conda env export > environment.yaml



创建新环境安装依赖：

conda env create -f environment.yaml



### pipenv

解决了旧的 pip+virtual en v+requ i rem en ts. txt 的 工 作方式的弊端 。 具体来说，它是pip 、和pfile 和 Virtualenv 的 结合体，它让包安装、包依赖 管理和虚拟环境管理更加方便，使用它可以 实 现高效 的 Python 项 目开 发工作流 。 







## MVC架构

![image-20240627120034339](https://raw.githubusercontent.com/h1s97x/picture/main/Doc/image-20240627120034339.png)

### 文档问题

多余空白内容：

str.strip()