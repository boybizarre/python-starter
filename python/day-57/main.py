import random
from datetime import datetime
from flask import Flask, render_template
import requests

GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"

API_KEY = "c4126cd287ed422a3918c8ccbc85c149"

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1,10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_num, year=current_year)

@app.route('/guess/<name>')
def get_gender_and_age(name):

    genderize_params = {
        "name": name
        # "apikey": API_KEY
    }

    agify_params = {
        "name": name
        # "apikey": API_KEY
    }

    genderize_response = requests.get(GENDERIZE_URL, params=genderize_params)
    agify_response = requests.get(AGIFY_URL, params=agify_params)

    genderize_response.raise_for_status()
    agify_response.raise_for_status()

    genderize_data = genderize_response.json()
    agify_data = agify_response.json()

    print(genderize_data, 'gender data')
    print(agify_data, 'age data')

    # return 'GENDER AND AGE'

    return render_template('gender_age.html', name=name, gender=genderize_data['gender'], age=agify_data['age'])


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/9b7ceeaa487328814501'

    response = requests.get(blog_url)

    response.raise_for_status()
    all_posts = response.json()

    # print(all_posts)

    # return 'HI'
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
