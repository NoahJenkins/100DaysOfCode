from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/login", methods= ["POST"])
def recieve_data():
    return "Data recieved!"

if __name__ == '__main__':
    app.run(debug=True)