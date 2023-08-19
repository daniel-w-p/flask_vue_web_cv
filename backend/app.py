from flask import Flask, jsonify, request
from .schemas import MA, user_schema, resume_schema
from .models import DB, User, Resume
from .secret import Psql

app = Flask(__name__)

DB.set(app, Psql)
db = DB.get()

MA.set(app)
ma = MA.get()


@app.route('/')
def invitation():
    return jsonify({"title": "CV Constructor"})


@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)


@app.route('/add', methods=['POST'])
def add_cv():
    title = request.json['title']
    name = request.json['name']
    address = request.json['address']


@app.route('/cv', methods=['GET'])
def get_cv():
    return jsonify({"title": "CV Constructor"})


if __name__ == '__main__':
    app.run()
