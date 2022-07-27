from app import app

from flask import render_template, session

from app.services.user_service import UserService

userservice = UserService()

@app.route('/user/<int:userid>')
def profile_page(userid: int):
    return render_template('user/user.html', user= userservice.find_one(userid))

@app.route('/login')
def login_page():
    print(session.get('username'))
    return render_template('user/login.html')
