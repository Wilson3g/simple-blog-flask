from flask import Flask, jsonify, request
import datetime

# Database imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Serealizing imports
from flask_marshmallow import Marshmallow, Schema

def create_app():
    app = Flask(__name__)

    # DB Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/simple_blog'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Serealizations
    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    # Migrations config
    Migrate(app, db)
    manage = Manager(app)
    manage.add_command('db', MigrateCommand)

    # Serealization class
    class UserSchema(ma.Schema):
        class Meta:
            fields = ('id', 'email', 'username', 'password')

    class CommentSchema(ma.Schema):
        class Meta:
            fields = ('id', 'comment', 'created_at' 'updated_at', 'user_id')

    # Models
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True) 
        email = db.Column(db.String(100)) 
        username = db.Column(db.String(50)) 
        password = db.Column(db.String(100)) 
        # is_admin = db.Column(db.String(10))

        def __init__(self, email, username, password):
            self.email = email
            self.username = username
            self.password = password
            # self.is_admin = is_admin


    class Comment(db.Model):
        id = db.Column(db.Integer, primary_key=True) 
        comment = db.Column(db.String(255)) 
        created_at = db.Column(db.String(50)) 
        updated_at = db.Column(db.String(100)) 
        user_id = db.Column(db.String(100)) 

        def __init__(self, comment, created_at, updated_at, user_id):
            self.comment = comment
            self.created_at = created_at
            self.updated_at = updated_at
            self.user_id = user_id

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)
    comment_schema = CommentSchema()
    comments_schema = CommentSchema(many=True)

    # Services and controllers

    @app.route('/user', methods=['GET'])
    def get_all_users():
        all_users = User.query.all()
        result = users_schema.dump(all_users)

        return jsonify({'users': result})

    @app.route('/user/<int:id>', methods=['GET'])
    def get_user(id):
        user = User.query.get(id)
        result = user_schema.dump(user)

        return jsonify({'users': result})

    @app.route('/user', methods=['POST'])
    def create_new_user():
        try:
            email = request.json['email']
            username = request.json['username']
            password = request.json['password']

            new_user = User(email, username, password)

            db.session.add(new_user)
            db.session.commit()

            return jsonify({'success': True}), 201
        except Exception as e:
            return jsonify({'erro': e})

    @app.route('/user/<int:id>', methods=['POST'])
    def update_user(id):
        user = User.query.get(id)

        user.email = request.json['email']
        user.username = request.json['username']
        user.password = request.json['password']

        db.session.commit()

        return user_schema.jsonify({'success': True}), 202

    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({'success': True})



    # COMMENTS CONTROLLER AND ROUTES
    @app.route('/comment', methods=['GET'])
    def get_all_comments():
        all_comments = Comment.query.all()
        result = comments_schema.dump(all_comments)

        return jsonify({'comments': result})

    @app.route('/comment/<int:id>', methods=['GET'])
    def get_comment(id):
        comment = Comment.query.get(id)
        comment_by_id = comment_schema.dump(comment)

        return comment_by_id

    @app.route('/comment', methods=['POST'])
    def create_new_comment():
        try:
            now = datetime.datetime.now()

            comment = request.json['comment']
            created_at = (now.strftime("%Y-%m-%d %H:%M:%S"))
            updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
            user_id = request.json['user_id']

            new_comment = Comment(comment, created_at, updated_at, user_id)

            db.session.add(new_comment)
            db.session.commit()

            return jsonify({'success': True}), 201
        except Exception as e:
            return jsonify({'erro': e})

    @app.route('/comment/<int:id>', methods=['POST'])
    def update_comment(id):
        now = datetime.datetime.now()

        comment = Comment.query.get(id)

        comment.comment = request.json['comment']
        comment.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

        db.session.commit()

        return jsonify({'success': True}), 202

    @app.route('/comment/<int:id>', methods=['DELETE'])
    def delete_comment(id):
        comment = Comment.query.get(id)

        db.session.delete(comment)
        db.session.commit()

        return jsonify({'success': True})

    return app