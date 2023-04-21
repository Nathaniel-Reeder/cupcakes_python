from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cupcakes')
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route('/cupcake_individual')
def individual_cupcake():
    return render_template("cupcake_individual.html")

@app.route('/order')
def order():
    return render_template('order.html')

if __name__ == "__main__":
    app.debug = 'development'
    app.run(debug = True, port = 8000, host = "localhost")