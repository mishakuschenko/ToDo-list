from init import *

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<int:userId>')
def userId(userId):
    return f"{userId}"
