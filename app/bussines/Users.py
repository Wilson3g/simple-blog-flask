from flask import Blueprint, jsonify, request, current_app
from ..model.Model import User, configure as db
from ..serealize.Serealize import UserSchema

bp_users = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@bp_users.route('/user', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify({'users': result})

@bp_users.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    result = user_schema.dump(user)

    return jsonify({'users': result})

@bp_users.route('/user', methods=['POST'])
def create_new_user():
    data_user_json = user_schema.load(request.json)

    email = data_user_json['email']
    username = data_user_json['username']
    password = data_user_json['password']
    
    new_user = User(email, username, password)

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return jsonify({'success': True}), 201

@bp_users.route('/user/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)

    data_user_json = user_schema.load(request.json)

    user.email = data_user_json['email']
    user.username = data_user_json['username']
    user.password = data_user_json['password']

    current_app.db.session.commit()

    return jsonify({'success': True}), 202

@bp_users.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    current_app.db.session.delete(user)
    current_app.db.session.commit()

    return jsonify({'success': True})
