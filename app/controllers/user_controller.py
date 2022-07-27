from app import app

from flask import jsonify, render_template, session, request

from app.services.user_service import UserService
from app.forms.user_register_form import UserRegisterform

userservice = UserService()

@app.route('/user/<int:userid>')
def profile_page(userid: int):
    return render_template('user/user.html', user= userservice.find_one(userid))

@app.route('/login')
def login_page():
    return render_template('user/login.html')

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