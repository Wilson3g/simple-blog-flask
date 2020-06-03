from flask import Flask
from flask_cors import CORS, cross_origin

# Database imports
from app.config.database import configure as config_db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Serealize import
from app.config.serealize import configure as config_ma

def create_app():
    app = Flask(__name__)

    CORS(app)

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

    # Import routes and controllers
    from .bussines.Users import bp_users
    app.register_blueprint(bp_users)

    from .bussines.Comments import bp_comments
    app.register_blueprint(bp_comments)

    from app.bussines.Posts import bp_comments
    app.register_blueprint(bp_comments)

    from app.bussines.Tags import bp_tags
    app.register_blueprint(bp_tags)

    return app