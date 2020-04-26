import os
import threading

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder="./frontend")   # static_folder="./dist/static", template_folder="./dist"


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)