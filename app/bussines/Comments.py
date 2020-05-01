from flask import Blueprint, jsonify, request, current_app
from ..model.Model import Comment, configure as db
from ..serealize.Serealize import CommentSchema
import datetime

bp_comments = Blueprint('comments', __name__)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@bp_comments.route('/comment', methods=['GET'])
def get_all_comments():
    all_comments = Comment.query.all()
    result = comments_schema.dump(all_comments)

    return jsonify({'comments': result})

@bp_comments.route('/comment/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get(id)
    comment_by_id = comment_schema.dump(comment)

    return comment_by_id

@bp_comments.route('/comment', methods=['POST'])
def create_new_comment():
    now = datetime.datetime.now()
    data_comment_json = comment_schema.load(request.json)

    # import ipdb; ipdb.set_trace()
    # return {}, 200

    comment = data_comment_json['comment']
    created_at = (now.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    user_id = data_comment_json['user_id']

    new_comment = Comment(comment, created_at, updated_at, user_id)

    current_app.db.session.add(new_comment)
    current_app.db.session.commit()

    return jsonify({'success': True}), 201

@bp_comments.route('/comment/<int:id>', methods=['POST'])
def update_comment(id):
    now = datetime.datetime.now()

    comment = Comment.query.get(id)

    comment.comment = request.json['comment']
    comment.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

    current_app.db.session.commit()

    return jsonify({'success': True}), 202

@bp_comments.route('/comment/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)

    current_app.db.session.delete(comment)
    current_app.db.session.commit()

    return jsonify({'success': True})