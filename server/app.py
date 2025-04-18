from flask import Flask, redirect , session , jsonify
from flask_cors import CORS
from flask_session import Session
from config.appconfig import DB_config , redis_config
from api.services.auth import login , signup , get_current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)

CORS(
    app,
    supports_credentials=True,
    origins="http://localhost:3000",
    allow_headers=["Content-Type", "Authorization"]
    )


bcrypt = Bcrypt(app)

DB_config(app=app)

redis_config(app=app)

Session(app=app)

@app.route('/api/')
def testing():
    return "<a>hello this is working really fine<a/>"

@app.route("/api/auth/signup",methods=["POST"])
def user_signup():
    return signup()

@app.route('/api/auth/login', methods=['POST'])
def user_login():
    response = login()
    return response

@app.route('/api/auth/current_user', methods=['GET'])
def current_user():
    return get_current_user()
    
    

if __name__ == "__main__":
    app.run(debug=True)