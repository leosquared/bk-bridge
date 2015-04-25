import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Error Log
if not app.debug:
    import logging
    from logging import FileHandler
    file_handler = FileHandler('error_log.txt')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def hello():
	return render_template('index.html')