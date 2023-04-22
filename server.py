from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake_by_name, add_cupcake_dictionary, order_price, remove_cupcake, find_cupcake_by_id

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cupcakes')
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("menu.csv"))

@app.route('/individual_cupcake/<name>')
def individual_cupcake(name):
    print(name)
    cupcake = find_cupcake_by_name("menu.csv", name)
    print(cupcake['sprinkles'])
    if cupcake:
        return render_template("cupcake_individual.html", cupcake=cupcake)
    else:
        return "Cupcake not found!"

@app.route('/order')
def order():
    return render_template('order.html', cupcakes = get_cupcakes("order.csv"), order_total = order_price('order.csv'))

@app.route('/add_cupcake/<name>')
def add_cupcake(name):
    cupcake = find_cupcake_by_name("menu.csv", name)
    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for('order'))
    else:
        return "Cupcake not found!"

@app.route('/remove_from_order/<id>')
def remove_from_order(id):
    cupcake = find_cupcake_by_id("order.csv", id)
    if cupcake:
        remove_cupcake('order.csv', cupcake)
        return redirect(url_for('order'))
    else:
        return "Cupcake not found in order!"

if __name__ == "__main__":
    app.debug = 'development'
    app.run(debug = True, port = 8000, host = "localhost")