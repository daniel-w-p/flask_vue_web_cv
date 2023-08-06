from flask import Flask, jsonify
from .models import DB
from .secret import Psql

app = Flask(__name__)

DB.set(app, Psql)


@app.route('/')
def invitation():
    return jsonify({"title": "CV Constructor"})


if __name__ == '__main__':
    app.run()
