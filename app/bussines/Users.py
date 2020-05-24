from flask import Blueprint, jsonify, request, current_app
from app.model.User import User
from app.config.database import configure as db
from app.serealize .user_serealize import UserSchema

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

    if user == None:
        return jsonify({
            'success': False,
            'message': 'Usuário inexistente'
        }), 401

    result = user_schema.dump(user)

    return jsonify({'users': result})

@bp_users.route('/user', methods=['POST'])
def create_new_user():
    data_user_json = user_schema.load(request.json)

    # Checa se todos os dados foram informados e se não tem não existem dados nulos
    if len(data_user_json) < 3 or "" in data_user_json.values():
        return jsonify({
            'success': False,
            'message': 'Você deve informar todos os dados!'
        }), 401

    email = data_user_json['email']
    username = data_user_json['username']
    password = data_user_json['password']

    new_user = User(email=email, username=username, password=password, is_admin=False)

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return jsonify({'success': True}), 201

@bp_users.route('/user/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)

    if user == None:
        return jsonify({
            'success': False,
            'message': 'Usuário inexistente'
        }), 401

    data_user_json = user_schema.load(request.json)

    if len(data_user_json) < 1 or '' in data_user_json.values():
        return jsonify({
            'success': False,
            'message': 'Informe todos os dados'
        }), 401

    user.username = data_user_json['username']
    current_app.db.session.commit()

    return jsonify({'success': True}), 202

@bp_users.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    
    if user == None:
        return jsonify({
            'success': False,
            'message': 'Usuário inexistente'
        }), 401

    current_app.db.session.delete(user)
    current_app.db.session.commit()

    return jsonify({'success': True})
