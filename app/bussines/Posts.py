from flask import Blueprint, jsonify, request, current_app
from app.model.Post import Post
from app.config.database import configure as db
from app.serealize.post_serealize import PostSchema
from marshmallow import EXCLUDE


bp_comments = Blueprint('posts', __name__)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@bp_comments.route('/post', methods=['GET'])
def get_all_users():
    p = Post.get_all()
    posts = posts_schema.dump(p)
    return jsonify(posts)

@bp_comments.route('/post/<_id>', methods=['GET'])
def find_post_by_id(_id):
    post = Post.search_by_id(_id)
    if not post:
        return {'error': 'Post não encontrado'}
    return post_schema.dump(post)

@bp_comments.route('/post/search/<search>', methods=['GET'])
def find_post_by_title(search):
    post = Post.query.filter(Post.title.like('%' + search + '%' )).all()

    return jsonify({'message': 'sucess', 'posts': posts_schema.dump(post)})


@bp_comments.route('/post', methods=['POST'])
def save_new_post():
    p = post_schema.load(request.json)
    p.save()
    return post_schema.dump(p)

@bp_comments.route('/post/<id>', methods=['PUT'])
def update_post(id):
    post = Post.search_by_id(id)
    if not post:
        return {'error': 'Post não encontrado'}, 404
    p = post_schema.load(request.json, instance=post, unknown=EXCLUDE)
    p.update()
    return post_schema.dump(p)

@bp_comments.route('/post/<_id>', methods=['DELETE'])
def delete_post(_id):
    p = Post.search_by_id(_id)
    if not p:
        return {'error': 'Post não encontrado'}
    p.delete()
    return {'success': 'Excluido com sucesso'}
