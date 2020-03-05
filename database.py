from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(60),nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

db.create_all()