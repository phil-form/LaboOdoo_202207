from app import app

from flask import render_template, session, request, url_for, redirect
from app.dtos.user_dto import UserDTO

from app.services.user_service import UserService
from app.forms.user_register_form import UserRegisterform
from app.forms.user_login_form import UserLoginform
from app.models.user import User
import os

userservice = UserService()

@app.route('/users')
def profile_list():
    return render_template('user/list.html', users=userservice.find_all())

@app.route('/users/<int:userid>', methods=['GET', 'POST'])
def profile_page(userid: int):
    return render_template('user/profile.html', user=userservice.find_one(entity_id=userid),
                                                profile_picture=url_for('static', filename='images/blank_profile.png'))

@app.route('/users/<int:userid>/edit', methods=['GET', 'POST'])
def edit_profile(userid: int):
    if request.method == "POST":
        form = UserRegisterform(request.form)
        user = userservice.update(userid, form)
        return redirect(url_for('profile_page', userid=userid))
    else:
        form = UserRegisterform(request.form)
        user = userservice.find_one(entity_id=userid)
        form.load_from_DTO(user)
        return render_template('user/profile_edit.html', user= user, form=form,
                                                         profile_picture=url_for('static', filename='images/blank_profile.png'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = UserLoginform(request.form)
    if request.method == "POST":
        if form.validate():
            user = userservice.login(form)

            if not type(user) == UserDTO:
                return render_template('user/login.html', form=form, errors=user)
            session['userid'] = user.user_id
            session['username'] = user.username
            return redirect(url_for('profile_page', userid=user.user_id))
        else:
            return render_template('user/login.html', form=form, errors=form.errors)        

    return render_template('user/login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register_page():
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
def logout():
    session.pop('userid')
    session.pop('username')
    return redirect(url_for('index'))