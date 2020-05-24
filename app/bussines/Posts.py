from flask import Blueprint, jsonify, request, current_app
from app.model.Post import Post
from app.config.database import configure as db
from app.serealize.post_serealize import PostSchema

bp_comments = Blueprint('posts', __name__)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@bp_comments.route('/post', methods=['GET'])
def get_all_users():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)

    return jsonify({'posts': result})

@bp_comments.route('/post/<_id>', methods=['GET'])
def find_post_by_id(_id):
    post = Post.query.get(_id)

    return jsonify({'success': True, 'post': post_schema.dump(post)})

@bp_comments.route('/post/search/<search>', methods=['GET'])
def find_post_by_title(search):
    post = Post.query.filter(Post.title.like('%' + search + '%' )).all()

    return jsonify({'message': 'sucess', 'posts': posts_schema.dump(post)})


@bp_comments.route('/post', methods=['POST'])
def save_new_post():
    request_post = request.json

    if len(request_post) < 3 or '' in request_post.values():
        return jsonify({'success': False, 'message': 'Informe todos os campos'})

    save = Post(
        title=request_post['title'], 
        content=request_post['content'], 
        author=request_post['author'])

    current_app.db.session.add(save)
    current_app.db.session.commit()

    return jsonify({'sucess': True, 'message':'cadastrado com sucesso', 'post': post_schema.dump(save)})

@bp_comments.route('/post/<id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({'success': None, 'message': 'Nenhum usuário encontrado'})

    if len(request.json) < 3 or '' in request.json.values():
        return jsonify({'success': True, 'message': 'Inform todos os dados'})

    post.title = request.json['title']
    post.content = request.json['content']
    post.author = request.json['author']

    current_app.db.session.commit()

    return jsonify({'success': True, 'message': 'Atualizado com sucess'})

@bp_comments.route('/post/<_id>', methods=['DELETE'])
def delete_post(_id):
    post = Post.query.get(_id)

    if not post:
        return jsonify({'success': False, 'message': 'Nenhum usuário encontrado'})

    current_app.db.session.delete(post)
    current_app.db.session.commit()

    return jsonify({'success': True, 'message': 'Deletado com sucesso'})