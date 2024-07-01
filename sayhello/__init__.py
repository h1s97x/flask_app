# -*- coding: utf-8 -*-
"""
"""
import os

from flask import Flask, render_template
from flask_login import current_user
from flask_wtf.csrf import CSRFError

import click
from faker import Faker  # 将Faker导入移动到文件顶部

from sayhello.extensions import bootstrap, db, login_manager, moment, oauth
from sayhello.models import Message
from sayhello.config import config  # 导入存储配置的字典

from sayhello.blueprints.hello import hello_bp

fake = Faker()  # 在文件级别创建一个Faker实例，避免在函数内部多次创建

def create_app(config_name=None):
    if config_name is None:
        # 从环境变量中获取FLASK_ENV，并设置默认值，同时确保它是有效的配置名称
        config_name = os.getenv('FLASK_ENV', 'development')
        if config_name not in config:
            raise ValueError(f"Invalid config name: {config_name}. Must be one of {list(config.keys())}")

    app = Flask('sayhello')

    # 导入配置，根据配置环境实例化对象
    app.config.from_object(config[config_name])
    # app.config.from_pyfile('settings.py')  # 从settings.py文件中读取配置

    # 注册扩展
    register_extensions(app)
    register_commands(app)
    register_blueprints(app)
    register_errorhandlers(app)

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)
    moment.init_app(app)
    oauth.init_app(app)

def register_blueprints(app):
    app.register_blueprint(hello_bp)

def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--count', default=20, help='Quantity of messages, default is 20.')
    def forge(count):
        """Generate fake messages."""
        # 输出提示信息
        click.echo('Working...')

        # 循环 count 次，生成假消息
        for i in range(count):
            message = Message(
                # 生成随机姓名
                name=fake.name(),
                # 生成随机句子
                body=fake.sentence(),
                # 生成今年内的随机日期时间
                timestamp=fake.date_time_this_year()
            )
            # 将生成的假消息添加到数据库会话中
            db.session.add(message)

        # 提交数据库会话，将假消息保存到数据库中
        db.session.commit()
        # 输出提示信息，显示生成的假消息数量
        click.echo('Created %d fake messages.' % count)

def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500
