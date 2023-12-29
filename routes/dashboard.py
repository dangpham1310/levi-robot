from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import db



@routes.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    username = session['username']

    user = User.query.filter_by(username=username).first()
    print(user.role)
    return redirect(url_for('routes.analysis'))

@routes.route('/analysis', methods=['POST','GET'])
def analysis():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    active_page = 'analysis'  # Set the active page here dynamically
    if request.method == 'POST':
        result_input = request.form.get('result-input')
        print("OK")
        f= open("message.txt","w",encoding="utf8")
        f.write(result_input)
        f.close()
        print("OK2")
        a = open("messageprev.txt","w",encoding="utf8")
        a.write(result_input)
        a.close()
        
    f= open("message.txt","r",encoding="utf8")
    data = f.readlines()
    f.close()

    f= open("messageprev.txt","r",encoding="utf8")
    prevdata = f.readlines()
    f.close()

    try:
        return render_template('analysis.html', active_page=active_page,data = data[0],prevdata = prevdata[0])
    except:
        return render_template('analysis.html', active_page=active_page,data = "")
    
@routes.route('/data', methods=["GET"])
def data():
    # if 'username' not in session:
    #     return redirect(url_for('routes.login'))

    with open("message.txt", "r", encoding="utf8") as f:
        data = f.read()

    return jsonify({"data": data})

@routes.route('/users')
def users():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    active_page = 'users'
    users = User.query.all()
    sorted_users = sorted(users, key=lambda user: user.id, reverse=True)
    print("OK")
    return render_template('users.html', active_page=active_page,users = sorted_users)


