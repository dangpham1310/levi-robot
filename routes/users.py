from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import db

from flask import render_template, request
from . import routes
from .db import User
from routes.db import db

@routes.route('/active', methods=['POST'])
def active():
    if request.method =="POST":
        user_name = request.form.get('user_name')
        user = User.query.filter_by(username=user_name).first()
        if user:
            user.status = "Active"
            db.session.commit()
            return redirect(url_for('routes.users'))
@routes.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        user_name = request.form.get('phoneNumber')

        user = User.query.filter_by(username=user_name.strip()).first()
        if user:
            return render_template('users.html', users=[user])
        else:
            users = User.query.all()
            return render_template('users.html', users=users)

        
@routes.route('/deactivate', methods=['POST'])
def deactivate():
    if request.method =="POST":
        user_name = request.form.get('user_name')
        user = User.query.filter_by(username=user_name).first()
        if user:
            user.status = "UnActive"
            db.session.commit()
            return redirect(url_for('routes.users'))
        
@routes.route('/edit', methods=['POST'])
def edit():
    if request.method =="POST":
        user_name = request.form.get('username')
        status = request.form.get('status_actives')
        newusername = request.form.get('newusername')
        link = request.form.get('link')
        print(user_name)
        print(status)
        user = User.query.filter_by(username=user_name).first()
        if user:
            if status != "" and status!= user.status:
                user.status = status
            if user_name!= newusername:
                user.username = newusername
            if  user.link != link:
                user.link = link
            db.session.commit()
            return redirect(url_for('routes.users'))
        
@routes.route('/changepass', methods=['POST',"GET"])
def changepass():
    if request.method =="POST":
        user_name = request.form.get('username')
        user = User.query.filter_by(username=user_name).first()
        user = User(username = user_name)

        changepass = request.form.get('changepass')
        user.set_password(changepass)
        db.session.commit()
        return redirect(url_for('routes.users'))
    return render_template('changepass.html', active_page="ChangePass")
@routes.route('/changepassadmin', methods=['POST',"GET"])
def changepassadmin():
    if request.method =="POST":
        # current_password = request.form.get("current_password")
        new_password= request.form.get("new_password")
        confirm_password= request.form.get("confirm_password")
        if new_password == confirm_password:
            user = User.query.filter_by(username="Admin").first()
            user.set_password(new_password)
            db.session.commit()
            return redirect(url_for('routes.users'))
        else:
            return "Mật khẩu xác nhận không chính xác"
    return render_template('changepass.html', active_page="ChangePass")
    
@routes.route('/delete', methods=['POST'])
def delete():
    if request.method =="POST":
        user_name = request.form.get('delete')
        user = User.query.filter_by(username=user_name).first()

        if user:
            print("Hehehehe")
            db.session.delete(user)
            db.session.commit()
        
    return redirect(url_for('routes.users'))
