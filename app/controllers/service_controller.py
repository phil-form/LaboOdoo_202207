from app import app
from flask import render_template, request, redirect, url_for, session

from app.forms.service_form import ServiceForm
from app.framework.decorators.inject import inject
from app.services.service_service import ServiceService

# TODO manage form errors


@app.route('/services', methods=['GET'])
@inject
def service_list(service_service: ServiceService):
    services = service_service.find_all()
    return render_template('service/service_list.html', services=services)


@app.route('/services/new', methods=['GET', 'POST'])
@inject
def service_add(service_service: ServiceService):
    form = ServiceForm(request.form)
    if request.method == 'POST':
        if form.validate():
            service = service_service.insert(form)
            return redirect(url_for('service_detail', service_id=service.service_id))
    print(form.errors)
    return render_template('service/service_form.html', service=None, form=form)


@app.route('/services/update/<int:service_id>', methods=['GET', 'POST'])
@inject
def service_update(service_id: int, service_service: ServiceService):
    service = service_service.find_one(service_id)
    form = ServiceForm(request.form)
    if request.method == 'POST':
        if form.validate():
            service = service_service.update(service_id, form)
            return redirect(url_for('service_detail', service_id=service.service_id))
    print(service)
    form.name.data = service.name
    form.service_type.data = service.type.name
    form.request.data = service.request
    form.description.data = service.description
    return render_template('service/service_form.html', service=service, form=form)


@app.route('/services/<int:service_id>', methods=['GET'])
@inject
def service_detail(service_id: int, service_service: ServiceService):
    service = service_service.find_one(service_id)
    print(service.users)
    return render_template('service/service_detail.html', service=service)


@app.route('/services/addUser/<int:service_id>', methods=['GET'])
@inject
def service_add_user(service_id: int, service_service: ServiceService):
    service = service_service.add_user(session.get("userid"), service_id)
    return render_template('service/service_detail.html', service=service)
