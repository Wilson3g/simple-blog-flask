from flask import Blueprint, jsonify, request, current_app
from app.model.User import User
from app.config.database import configure as db
from app.serealize .user_serealize import UserSchema
from marshmallow import EXCLUDE

bp_users = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@bp_users.route('/user', methods=['GET'])
def get_all_users():
    u = User.show_all_users()
    listing = users_schema.dump(u)
    return jsonify(listing)

@bp_users.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    u = User.query.get(id)
    if not u:
        return {'erro': 'Usuário não encontrado'}
    return user_schema.dump(u)

@bp_users.route('/user', methods=['POST'])
def create_new_user():
    u = user_schema.load(request.json)
    check = User.check_email_exists(u.email)
    if check:
        return {'error': 'Email já existe!'}
    u.save()

    return user_schema.dump(u)

@bp_users.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    usuario = User.search_by_id(id)
    u = user_schema.load(request.json, instance=usuario, unknown=EXCLUDE)
    u.update()

    return user_schema.dump(u)

@bp_users.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    u = User.search_by_id(id)
    if not u:
        return {'erro': 'Usuário não encontrado'}
    u.delete()
    return {'success': 'Deletado com sucesso'}
