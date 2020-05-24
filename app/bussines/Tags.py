from flask import Blueprint, jsonify, request, current_app
from app.model.Tags import Tag
from app.config.database import configure as db
from app.serealize.tags_serealize import TagSchema

bp_tags = Blueprint('tags', __name__)

tag_schema = TagSchema()
tags_schema = TagSchema(many=True)

@bp_tags.route('/tags', methods=['GET'])
def get_all_tags():
    all_tags = Tag.query.all()
    result = tags_schema.dump(all_tags)

    return jsonify({'result': result})

@bp_tags.route('/tags/<_id>', methods=['GET'])
def find_post_by_id(_id):
    post = Tag.query.get(_id)

    return jsonify({'success': True, 'post': tag_schema.dump(post)})

@bp_tags.route('/tags', methods=['POST'])
def save_new_post():
    request_tag = request.json

    if len(request_tag) < 1 or '' in request_tag.values():
        return jsonify({'success': False, 'message': 'Informe todos os campos'})

    save = Tag(name=request_tag['name'])
    current_app.db.session.add(save)
    current_app.db.session.commit()

    return jsonify({'sucess': True, 'message':'cadastrado com sucesso', 'post': tag_schema.dump(save)})

@bp_tags.route('/tags/<id>', methods=['PUT'])
def update_post(id):
    tag = Tag.query.get(id)

    if not tag:
        return jsonify({'success': None, 'message': 'Nenhum usuário encontrado'})

    if len(request.json) < 1 or '' in request.json.values():
        return jsonify({'success': True, 'message': 'Inform todos os dados'})

    tag.name = request.json['name']
    current_app.db.session.commit()

    return jsonify({'success': True, 'message': 'Atualizado com sucess'})

@bp_tags.route('/tags/<_id>', methods=['DELETE'])
def delete_tag(_id):
    tag = Tag.query.get(_id)

    if not tag:
        return jsonify({'success': False, 'message': 'Nenhum usuário encontrado'})

    current_app.db.session.delete(tag)
    current_app.db.session.commit()

    return jsonify({'success': True, 'message': 'Deletado com sucesso'})