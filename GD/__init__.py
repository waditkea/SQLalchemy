from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import app_config
db=SQLAlchemy()#creat SQLalchemy instance


def creat_app(config_name):
    application=Flask(__name__)
    application.config.from_object(app_config[config_name])
    from GD.Services.views import mod as user_module
    application.register_blueprint(user_module)
    db.init_app(application)#deploying app over database
    with application.app_context():#application context opens and close itself
        db.create_all()#to creat all tables
    return application

