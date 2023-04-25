import requests
import json as js


def get_weather(city, appid):
    params = {
        'q': city,
        'appid': appid
    }
    url = f'https://samples.openweathermap.org/data/2.5/weather'
    response = requests.get(url=url, params=params)
    
    if response.ok:
        with open(f'{city}_weather.json', 'w') as f:
            js.dump(response.json(), f)
    else:
        return response.status_code
    

if __name__ == '__main__':
    get_weather(city='moscow', appid='b6907d289e10d714a6e88b30761fae22')