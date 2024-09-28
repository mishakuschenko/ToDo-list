from init import *

@app.route('/')
def home():
    return render_template('index.html')


