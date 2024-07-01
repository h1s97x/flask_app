# -*- coding: utf-8 -*-
"""
"""
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_whooshee import Whooshee

# from flask_oauthlib.client import OAuth
from authlib.integrations.flask_client import OAuth

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()
oauth = OAuth()
csrf = CSRFProtect()
whooshee = Whooshee()
