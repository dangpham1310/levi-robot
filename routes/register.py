from flask import render_template, request
from . import routes
from .db import User
from routes.db import db
@routes.route('/registermanager', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            return "Tài khoản này đã tồn tại"
        user = User(username = username,password = password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return "Đăng kí thành công"

    return render_template('register.html')