from flask import Flask
import datetime

# Database imports
from .model.Model import configure as config_db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Serealize import
from .serealize.Serealize import configure as config_ma

def create_app():
    app = Flask(__name__)

    # DB Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/simple_blog'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    # Migrations config
    Migrate(app, app.db)
    manage = Manager(app)
    manage.add_command('db', MigrateCommand)

    from .bussines.Bussines import bp_books
    app.register_blueprint(bp_books)

    return app