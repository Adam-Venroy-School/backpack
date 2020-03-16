from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////backpack.db'
db = SQLAlchemy(app)

#Content Table
class Content(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(60),nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
