from flask import Flask


# TODO: Move config here later
app = Flask(__name__)
app.config['TESTING'] = True