from flask import Flask, render_template, jsonify,request,redirect,url_for

from routes import routes
from routes.db import db
import requests
app = Flask(__name__)
app.secret_key = 'n9b9monkey123456789'
app.register_blueprint(routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db?password=n9b9monkey'

db.init_app(app)


@app.route('/getdata')
def index():
    
    a = open("message.txt","r",encoding="utf8")
    datas =  a.readlines()
    a.close()
    try:
        data = {
            'TiLe': datas[0].split("|")[0],
            'InputAdmin': datas[0].split("|")[1]
        }

        return jsonify(data)
    except:
        data = {
            "Status":datas[0].split("|")[0]
        }
        return jsonify(data)
@app.route('/send_data', methods=['POST'])
def send_data():
    if request.method == "POST":
        TiLe = request.form.get("TiLe")
        InputAdmin = request.form.get("InputAdmin")

        
        if TiLe:
            pass
        if InputAdmin:
            pass

        f= open("message.txt","w",encoding="utf8")
        f.write(f'{TiLe}|{InputAdmin}|')
        f.close()

        result_input =  request.form.get('result-input')
        if result_input:
            f= open("message.txt","w",encoding="utf8")
            f.write(f'{result_input}|')
            f.close()

        return redirect(url_for('routes.dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5004,debug=False)
