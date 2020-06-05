from flask import Blueprint, jsonify, request, current_app
from app.model.Comment import Comment
from app.config.database import configure as db
from app.serealize.comment_serealize import CommentSchema
import datetime

bp_comments = Blueprint('comments', __name__)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@bp_comments.route('/comment/<int:id>', methods=['GET'])
def get_comment(_id):
    comment = Comment.find_by_id(_id)
    return comment_schema.dump(comment)

@bp_comments.route('/comment', methods=['POST'])
def create_new_comment():
    c = comment_schema.load(request.json)
    c.save()
    return comment_schema.dump(c)

@bp_comments.route('/comment/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.find_by_id(id)
    c = comment_schema.load(request.json, instance=comment)
    c.update()
    return comment_schema.dump(c)

@bp_comments.route('/comment/<int:id>', methods=['DELETE'])
def delete_comment(id):
    c = Comment.find_by_id(id)
    c.delete()
    return {'success': 'deletado com sucesso'}