from flask import Blueprint, jsonify, request
from ..model.Model import User, Comment, configure as db
from ..serealize.Serealize import UserSchema, CommentSchema

bp_books = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@bp_books.route('/user', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify({'users': result})

@bp_books.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    result = user_schema.dump(user)

    return jsonify({'users': result})

@bp_books.route('/user', methods=['POST'])
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

@bp_books.route('/user/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)

    user.email = request.json['email']
    user.username = request.json['username']
    user.password = request.json['password']

    db.session.commit()

    return user_schema.jsonify({'success': True}), 202

@bp_books.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({'success': True})



#  COMMENTS CONTROLLER AND ROUTES
@bp_books.route('/comment', methods=['GET'])
def get_all_comments():
    all_comments = Comment.query.all()
    result = comments_schema.dump(all_comments)

    return jsonify({'comments': result})

@bp_books.route('/comment/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get(id)
    comment_by_id = comment_schema.dump(comment)

    return comment_by_id

@bp_books.route('/comment', methods=['POST'])
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

@bp_books.route('/comment/<int:id>', methods=['POST'])
def update_comment(id):
    now = datetime.datetime.now()

    comment = Comment.query.get(id)

    comment.comment = request.json['comment']
    comment.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

    db.session.commit()

    return jsonify({'success': True}), 202

@bp_books.route('/comment/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)

    db.session.delete(comment)
    db.session.commit()

    return jsonify({'success': True})