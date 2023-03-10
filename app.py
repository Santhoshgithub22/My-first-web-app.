from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/demo")
def welcome():
    return render_template("index.html")

@app.route("/intro")
def intro():
    return "<h1> Welcome to the Santhosh Stationary <h1>"

@app.route("/shop", methods=['POST'])
def stationary():

    if (request.method=='POST'):
        product = request.json['product']
        price = request.json['price']
        count = request.json['count']
        result = 0

    if product == "Geometry Box":
        result = result + (price * count)

    return render_template("result.html", result = result)
    
@app.route("/shoppify", methods=['POST'])
def stationary_items():

    if (request.method=='POST'):
        product = request.form['product']
        price = request.form['price']
        count = request.form['count']
        result = 0

    if product == "Geometry Box":
        result = result + (price * count)

    return render_template("result.html", result = result)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

