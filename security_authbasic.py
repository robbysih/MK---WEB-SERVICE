#curl -u john:hello http://127.0.0.1:7002/

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "robby": generate_password_hash("hello"),
    "gusti": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug = True, port=7002)
