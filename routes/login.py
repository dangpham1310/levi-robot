from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import db

@routes.route('/', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if (not user or not user.check_password(password)):
            return "Invalid username or password"
        session['username'] = username
        if user.role == "Admin":
            return redirect(url_for('routes.dashboard'))
        if user.status == "UnActive":
            return "Not Active"
        else:
            return "Active"
    return render_template('login.html')
