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
    request_post = request.json

    if len(request_post) < 1 or '' in request_post.values():
        return jsonify({'success': False, 'message': 'Informe todos os campos'})
    print()
    save = Tag(name=request_post['name'])
    current_app.db.session.add(save)
    current_app.db.session.commit()

    return jsonify({'sucess': True, 'message':'cadastrado com sucesso', 'post': tag_schema.dump(save)})

# @bp_comments.route('/post/<id>', methods=['PUT'])
# def update_post(id):
#     post = Post.query.get(id)

#     if not post:
#         return jsonify({'success': None, 'message': 'Nenhum usuário encontrado'})

#     if len(request.json) < 3 or '' in request.json.values():
#         return jsonify({'success': True, 'message': 'Inform todos os dados'})

#     post.title = request.json['title']
#     post.content = request.json['content']
#     post.author = request.json['author']

#     current_app.db.session.commit()

#     return jsonify({'success': True, 'message': 'Atualizado com sucess'})

# @bp_comments.route('/post/<_id>', methods=['DELETE'])
# def delete_post(_id):
#     post = Post.query.get(_id)

#     if not post:
#         return jsonify({'success': False, 'message': 'Nenhum usuário encontrado'})

#     current_app.db.session.delete(post)
#     current_app.db.session.commit()

#     return jsonify({'success': True, 'message': 'Deletado com sucesso'})