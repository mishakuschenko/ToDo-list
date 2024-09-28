from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDo(db.Model):

    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    isComplete = db.Column(db.Boolean)

