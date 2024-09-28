from flask import Flask, render_template
from models import ToDo, db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()


@app.get('/')
def home():
    return render_template('index.html')


@app.get('/')
def add():
    pass


@app.get('/')
def update():
    pass


@app.get('/')
def delete():
    pass
