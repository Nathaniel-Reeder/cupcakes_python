from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, order_price, remove_cupcake

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cupcakes')
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("menu.csv"))

@app.route('/cupcake_individual')
def individual_cupcake():
    return render_template("cupcake_individual.html")

@app.route('/order')
def order():
    return render_template('order.html', cupcakes = get_cupcakes("order.csv"), order_total = order_price('order.csv'))

@app.route('/add_cupcake/<name>')
def add_cupcake(name):
    cupcake = find_cupcake("menu.csv", name)
    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for('order'))
    else:
        return "Cupcake not found!"

@app.route('/remove_from_order/<name>')
def remove_from_order(name):
    cupcake = find_cupcake("order.csv", name)
    if cupcake:
        remove_cupcake('order.csv', cupcake)
        return redirect(url_for('order'))
    else:
        return "Cupcake not found in order!"

if __name__ == "__main__":
    app.debug = 'development'
    app.run(debug = True, port = 8000, host = "localhost")