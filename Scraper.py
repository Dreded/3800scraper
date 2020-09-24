from flask import Flask, url_for, render_template
from flaskwebgui import FlaskUI   # get the FlaskUI class
import neweggCanada


app = Flask(__name__)
ui = FlaskUI(app)                 # feed the parameters


# do your logic as usual in Flask
stores = {}

@app.route("/")
def index(): 
    neweggStock = neweggCanada.get_stock()
    stores[neweggStock['title']] = neweggStock
    inStock = False
    if len(neweggStock[1]) > 0:
        inStock = True
    # context = {
    #     'title': neweggStock[2],
    #     'stock': neweggStock[0],
    #     'nostock': neweggStock[1],
    #     'inStock': inStock
    # }
    context = {
        'stores': neweggStock
    }
    return render_template('index.html', **context)


ui.run()                           # call the 'run' method 