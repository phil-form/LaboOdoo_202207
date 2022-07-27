from app import app
from app.services.comment_service import CommentService
from flask import render_template, redirect, jsonify
from app.framework.decorators.inject import inject

@app.route('/comments', methods=['GET'])
def get_comments():
    return render_template('comment/comment.html')


@app.route('/comments/service', methods=['GET', 'POST'])
@inject
def get_comments_by_service(comment_service: CommentService):
    service_id = 1

    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all_by(service_id=service_id)])


@app.route('/comments/user_service', methods=['GET', 'POST'])
@inject
def get_comments_by_user_service(comment_service: CommentService):
    user_service_id = 1

    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all_by(user_service_id=user_service_id)])
