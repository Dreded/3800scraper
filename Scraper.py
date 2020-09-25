from flask import Flask, render_template, session, request
from flaskwebgui import FlaskUI   # get the FlaskUI class

import glob
plugins = glob.glob('./store_plugins/store_*.py')

app = Flask(__name__)
app.secret_key = 'app secret key'
ui = FlaskUI(app)
newRun = True

@app.route("/", methods=['GET', 'POST'])
def index():
    global newRun
    if newRun:
        session['audio'] = False
        newRun = False

    if request.method == 'POST':
        if request.form['audio'] == 'Enable_Audio':
            session['audio'] = True
        elif request.form['audio'] == 'Disable_Audio':
            session['audio'] = False

    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    stores = {}
    for plugin in plugins:
        get_stock = __import__(plugin[2:-3].replace('\\','.'), fromlist=[None]).get_stock
        stores[plugin[22:-3]] = get_stock()

    context = {
        'title': '3080 Stock Tracker',
        'stores': stores,
        'refreshed': session['counter'],
        'audio': session['audio'],
    }
    return render_template('index.jinja', **context)

ui.run()                           # call the 'run' method 
