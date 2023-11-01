from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

# name = "Noah"

# genderize_url = "https://api.genderize.io"
# gender_params = {"name": name}

# gender_response = requests.get(url=genderize_url, json=gender_params)
# gender_response.raise_for_status()
# gender_data = gender_response.json()
# print(gender_data)


# agify_url = "https://api.agify.io"
# age_params = {"name": name}

# age_reponse = requests.get(url=agify_url, json=age_params)
# age_reponse.raise_for_status()
# age_data = age_reponse.json()
# print(age_data)



@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    return render_template("guess.html", person_name=name)


if __name__ == "__main__":
    app.run(debug=True)


