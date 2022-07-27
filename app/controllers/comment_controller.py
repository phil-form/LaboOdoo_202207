from app import app
from app.services.comment_service import CommentService
from flask import render_template, request, redirect, url_for, jsonify
from app.framework.decorators.inject import inject
from app.forms.comment.comment_add_form import CommentAddForm

@app.route('/comments', methods=['GET'])
def get_comments():
    return render_template('comment/comment.html')

@app.route('/comments/all', methods=['GET'])
@inject
def get_all_comments(comment_service: CommentService):
    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all()])


@app.route('/comments/add', methods=['GET', 'POST'])
@inject
def add_comment(comment_service: CommentService):
    form = CommentAddForm(request.form)

    if request.method == 'POST':
        if form.validate():
            try:
                comment = comment_service.insert(form)
                return redirect(url_for('get_all_comments'))
            except Exception as e:
                print(e)

    return render_template('comment/new_comment.html', form=form)


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
