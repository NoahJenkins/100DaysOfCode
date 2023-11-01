from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    print(gender)

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/d1b98697cc5200aae311"
    response = requests.get(blog_url)
    response.raise_for_status()
    data = response.json()
    
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)


