from flask import Flask

app = Flask(__name__)
###############################################################################################################################
#Rendering HTML

#If you spin run the application and access the site, you can inspect the HTML and see the text below in the various elements. 
@app.route("/")
def hello_world():
    return """
    <h1>Hello, World!</h1>
    <p1>This is a paragraph.</p>
    <img src="https://imgs.search.brave.com/xvvGnk0zqBUA0YmR20NLpPn8WZfA1iqs6ozKyPO-0B4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjI2/NDY0MTU4L3Bob3Rv/L2NhdC13aXRoLW9w/ZW4tbW91dGguanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPVFy/OURDVmt3S21fZHpm/amtlTjVmb0NCcDdj/M0VmQkZfaTJBMGV0/WWlKT0E9">
    """

###############################################################################################################################

@app.route("/bye")
def bye():
    return "Bye!"

###############################################################################################################################
#Variable Rules
#Link to documentation: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

#You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the
#<variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument
#like <converter:variable_name>.

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

###############################################################################################################################


if __name__ == "__main__":
    app.run(debug=True)