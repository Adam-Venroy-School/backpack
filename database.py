from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////backpack.db'
db = SQLAlchemy(app)

<<<<<<< HEAD

=======
#Content Table
>>>>>>> e72323b1e8a9c6e4e75a60f8a7ab020155632863
class Content(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(60),nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
