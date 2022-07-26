from app import app

from flask import render_template

from app.services.user_service import UserService

userservice = UserService()

@app.route('/user/<int:userid>')
def profile_page(userid: int):
    return render_template('user/user.html',user= userservice.find_one(userid))

