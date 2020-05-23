import os
from flask import Flask,render_template
import requests

def create_app(test_config=None):
    app = Flask(__name__)

    # print(app.instance_path)
    # print(__name__)
    @app.route('/')
    @app.route('/<country>')
    def hello(country='india'):
        response = requests.get('https://api.covid19api.com/total/dayone/country/'+country)
        print(response.json())
        json = response.json()
        for value in json:
            del value['CountryCode']
            del value['Province']
            del value['City']
            del value["CityCode"]
            del value['Lat']
            del value['Lon']

        return render_template('index.html', json=json)

    @app.route('/about')
    def about():
        return render_template('about.html')

    return app

# if __name__ == "__main__":
#     create_app()
#  instance_relative_config=True