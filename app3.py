from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('todo.html')


@app.route("/product")
def product():
    return "this is my product"

if __name__=="__main__":
    app.run(debug=True)