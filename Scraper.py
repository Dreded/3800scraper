from flask import Flask, render_template, session, request
from flaskwebgui import FlaskUI   # get the FlaskUI class
import multiprocessing
import time
import glob

app = Flask(__name__)
app.secret_key = 'app secret key'
ui = FlaskUI(app)
newRun = True
stores = {}
_pool = None

def process_plugin(plugin):
    get_stock = __import__(plugin[2:-3].replace('\\','.'), fromlist=[None]).get_stock
    return get_stock()

@app.route("/", methods=['GET', 'POST'])
def index():
    start_time = time.time()
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

    plugins = glob.glob('./store_plugins/store_*.py')
    output = _pool.map(process_plugin, plugins)
    for i,plugin in enumerate(plugins):
        #stores[plugin[22:-3]] = process_plugin(plugin)
        stores[plugin[22:-3]] = output[i]

    context = {
        'title': '3080 Stock Tracker',
        'stores': stores,
        'refreshed': session['counter'],
        'audio': session['audio'],
    }
    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template('index.jinja', **context)
if __name__ == '__main__':
    _pool = multiprocessing.Pool()
    try:
        ui.run()                           # call the 'run' method
    except KeyboardInterrupt:
        _pool.close()
        _pool.join()
        print("Processes complete, ready to finish")