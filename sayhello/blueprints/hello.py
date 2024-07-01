# -*- coding: utf-8 -*-
"""

"""
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint
from flask_login import current_user

from sayhello.forms import HelloForm
from sayhello.models import Message
from sayhello.extensions import db


hello_bp = Blueprint('hello', __name__)


@hello_bp.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('hello.index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)


@hello_bp.route('/about')
def about():
    return render_template('about.html')

