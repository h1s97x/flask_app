# -*- coding: utf-8 -*-
"""
"""
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

# 基础配置，使用继承的方式
class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data.db')

    # Google Oauth2.0
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', "<your-id-ending-with>.apps.googleusercontent.com")
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', "<your-secret>")
    GOOGLE_REQUEST_TOKEN_URL = os.getenv('GOOGLE_REQUEST_TOKEN_URL', "https://accounts.google.com/o/oauth2/auth")
    
    # Github OAuth2.0
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', 'Ov23ctoHnbS9GqRiihyV')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '2fe428f0157b077522fbc03a5f933e24e34e27d4')
    GITHUB_REQUEST_TOKEN_URL = os.environ.get('GITHUB_REQUEST_TOKEN_URL', "https://github.com/login/oauth/authorize")

    # GitLab OAuth2.0
    GITLAB_CLIENT_ID = os.environ.get('GITLAB_CLIENT_ID', '**************************************')
    GITLAB_CLIENT_SECRET = os.environ.get('GITLAB_CLIENT_SECRET', '**************************************')
    GITLAB_REQUEST_TOKEN_URL = os.environ.get('GITLAB_REQUEST_TOKEN_URL', "https://gitlab.com/oauth/authorize")
    # "https://gitlab.com/users/identity_verification/success https://gitlab.com/users/sign_up/welcome"

    OAUTH_CREDENTIALS={
        'google': {
            'id': GOOGLE_CLIENT_ID,
            'secret': GOOGLE_CLIENT_SECRET
        },
        'github': {
            'id': GITHUB_CLIENT_ID,
            'secret': GITHUB_CLIENT_SECRET
        },
        'gitlab': {
            'id': GITLAB_CLIENT_ID,
            'secret': GITLAB_CLIENT_SECRET
        },
    }

    # 从环境变量读取MySQL配置
    # MySQL所在主机名，默认127.0.0.1
    MYSQL_HOST = os.getenv('MYSQL_HOST', "127.0.0.1")
    # MySQL监听的端口号，默认3306
    MYSQL_PORT = os.getenv('MYSQL_PORT', 3306)
    # 连接MySQL的用户名
    MYSQL_USER = os.getenv('MYSQL_USER', "root")
    # 连接MySQL的密码
    MYSQL_PASS = os.getenv('MYSQL_PASS', "root")
    # MySQL上创建的数据库名称
    MYSQL_DB = os.getenv('MYSQL_DB', "database_learn")

    # 通过修改以下代码来操作不同的SQL比写原生SQL简单很多 --》通过ORM可以实现从底层更改使用的SQL
    # 根据环境变量动态生成SQLAlchemy URI
    # @property
    # def SQLALCHEMY_DATABASE_URI(self):
    #     if os.getenv('USE_SQLITE', False):
    #         return prefix + os.path.join(basedir, 'data.db')
    #     else:
    #         return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASS}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}?charset=utf8mb4"


class DevelopmentConfig(BaseConfig):
    """
    开发环境
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    生产环境
    """
    DEBUG = False


class TestingConfig(BaseConfig):
    """
    测试环境
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    # 在测试环境中，使用内存数据库
    USE_SQLITE = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database
    
# 映射环境对象
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}


# 通过环境变量来设置配置
# export FLASK_ENV=development
# export FLASK_ENV=production
# export FLASK_ENV=testing

