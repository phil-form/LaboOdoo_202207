from flask import request, render_template, session

from app import app
from app.forms.message_form import MessageForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.message_service import MessageService


@app.route('/messages/<int:user_id>', methods=['GET', 'POST'])
@inject
@auth_required()
def message_between(user_id: int, message_service: MessageService):
    form = MessageForm(request.form)
    form.to_user_id.data = user_id
    messages = message_service.find_all_between(user_id, session.get('userid'))
    if request.method == 'POST':
        message_service.insert(form)
    return render_template('message/conversation.html', messages=messages, form=form, errors=form.errors)
