from flask import Flask, render_template, request, redirect, url_for
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
    todo_list = ToDo.query.all()
    return render_template('index.html', todo_list=todo_list, title="main page")


@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = ToDo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))
    

@app.get('/')
def update():
    pass


@app.get('/')
def delete():
    pass
