from django.shortcuts import render
from dotenv import load_dotenv

import json
import urllib.request
import os
import unidecode

# Create your views here.

# https://stackoverflow.com/questions/52030957/how-to-hide-google-map-api-key-in-django-before-pushing-it-on-github
# Second way to define enviroment variables
def index(request):
    if(request.method == 'POST'):
        city = request.POST['city']

        format_city_name = city.replace(' ', '+')

        #https://stackoverflow.com/questions/34713619/use-accented-characters-with-rest-api-parse
        format_city_name = unidecode.unidecode(format_city_name)

        load_dotenv()

        resp = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+format_city_name+'&appid=' + os.getenv('OPEN_WEATHER_MAP_API_KEY')).read()

        json_data = json.loads(resp)

        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+ 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
        print(data)
    else:
        city = ''
        data = {}
        print('Hey here!!')

    return render(request, 'index.html', {'city': city, 'data': data})