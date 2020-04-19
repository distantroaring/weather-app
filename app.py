import requests 
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] =True


@app.route('/', methods=['GET', 'POST'])
def index():
    city = 'Dhaka'
    if request.method == 'POST':
        city = request.form.get('city')


    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a2e61e79076fcb6de5c59bfdfc0da652'
    
    r = requests.get(url.format(city)).json()
    
    
    try: 
        weather = {
            'city' : city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],

        }
        return render_template('weather1.html', weather = weather)
    except (IndexError, KeyError, TypeError):
        weather = {
            'city' : 'No City Found',
            'temperature': '',
            'description': '',
            'icon': '',

        }
        return render_template('weather1.html', weather = weather)        


if __name__ == '__main__':
    app.run()

