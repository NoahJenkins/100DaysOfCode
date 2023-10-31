from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("example_cv.html")

@app.route("/noah")
def noah():
    return render_template("personal_site.html")

if __name__ == "__main__":
    app.run(debug=True)