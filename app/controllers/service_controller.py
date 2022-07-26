from app import app
from flask import render_template, request, redirect, url_for, session

from app.forms.search_service_form import SearchServiceForm
from app.forms.service_form import ServiceForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.service_service import ServiceService


@app.route('/services', methods=['GET', 'POST'])
@inject
def service_list(service_service: ServiceService):
    form = SearchServiceForm(request.form)
    if request.method == 'GET':
        services = service_service.find_all()
    else:
        services = service_service.find_all_by(form)
    return render_template('service/service_list.html', services=services, form=form)

@app.route('/services/new', methods=['GET', 'POST'])
@auth_required()
@inject
def service_add(service_service: ServiceService):
    form = ServiceForm(request.form)
    if request.method == 'POST':
        if form.validate():
            service = service_service.insert(form)
            return redirect(url_for('service_detail', service_id=service.service_id))
    return render_template('service/service_form.html', service=None, form=form, errors=form.errors)


@app.route('/services/update/<int:service_id>', methods=['GET', 'POST'])
@auth_required()
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
    return render_template('service/service_form.html', service=service, form=form, errors=form.errors)


@app.route('/services/<int:service_id>', methods=['GET'])
@inject
def service_detail(service_id: int, service_service: ServiceService):
    service = service_service.find_one(service_id)
    return render_template('service/service_detail.html', service=service)


@app.route('/services/addUser/<int:service_id>', methods=['GET'])
@auth_required()
@inject
def service_add_user(service_id: int, service_service: ServiceService):
    service = service_service.add_user(session.get("userid"), service_id)
    return render_template('service/service_detail.html', service=service)
