from flask import request, render_template, session

from app import app
from app.forms.message_form import MessageForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.message_service import MessageService


@app.route('/messages/<int:user_id>', methods=['GET', 'POST'])
@auth_required()
@inject
def message_between(user_id: int, message_service: MessageService):
    form = MessageForm(request.form)
    form.to_user_id.data = user_id

    if request.method == 'POST':
        print(form.to_user_id.data)
        message_service.insert(form)

    messages = message_service.find_all_between(user_id, session.get('userid'))
    return render_template('message/conversation.html', messages=messages, form=form, errors=form.errors)
