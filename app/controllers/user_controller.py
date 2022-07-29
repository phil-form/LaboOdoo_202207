from flask import render_template, session, request, url_for, redirect

from app import app
from app import db

from app.models.role    import Role
from app.models.user    import User
from app.dtos.user_dto  import UserDTO

from app.forms.user_register_form import UserRegisterform
from app.forms.user_login_form    import UserLoginform

from app.services.user_service    import UserService

from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject        import inject


@app.route('/users')
@inject
def profile_list(userservice: UserService):
    return render_template('user/list.html', users=userservice.find_all())

@app.route('/users/<int:userid>', methods=['GET'])
@inject
def profile_page(userid: int, userservice: UserService):
    return render_template('user/profile.html', user=userservice.find_one(entity_id=userid),
                                                profile_picture=url_for('static', filename='images/blank_profile.png'))

@app.route('/users/<int:userid>/edit', methods=['GET', 'POST'])
@auth_required()
@inject
def edit_profile(userid: int, userservice: UserService):
    form = UserRegisterform(request.form)
    if request.method == "POST":        
        user = userservice.update(userid, form)
        return redirect(url_for('profile_page', userid=userid))

    user = userservice.find_one(entity_id=userid)
    form.load_from_DTO(user)
    return render_template('user/profile_edit.html', user= user, form=form,
                                                        profile_picture=url_for('static', filename='images/blank_profile.png'))


@app.route('/login', methods=['GET', 'POST'])
@inject
def login_page(userservice: UserService):
    form = UserLoginform(request.form)
    if request.method == "POST":
        if form.validate():
            user = userservice.login(form)

            if not type(user) == UserDTO:
                return render_template('user/login.html', form=form, errors=user)
            session['userid'] = user.user_id
            session['username'] = user.username
            return redirect(url_for('profile_page', userservice=userservice, userid=user.user_id))
        else:
            return render_template('user/login.html', form=form, errors=form.errors)        

    return render_template('user/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
@inject
def register_page(userservice: UserService):
    form = UserRegisterform(request.form)
    if request.method == "POST":
        if form.validate():
            try:
                userservice.insert(form.get_as_userDTO())
                return render_template('user/register_ok.html')
            except Exception as e:
                print(e)
                return render_template('home/error.html')
        else:
            return render_template('user/register.html', form=form, errors=form.errors)
    return render_template('user/register.html', form=form)

@app.route('/logout')
@auth_required()
def logout():
    session.pop('userid')
    session.pop('username')
    return redirect(url_for('index'))

@app.route('/test')
@inject
def test(userservice: UserService):
    role = Role.query.filter_by(rolename='USER').first()
    user = User.query.filter_by(user_id=1).first()
    userservice.add_role(user.user_id, role)
    return render_template('layout/layout.html')