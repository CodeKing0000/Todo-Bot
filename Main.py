import requests

def get_wether(city, day):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload  = {'q': city,
            'cnt': 'day'
            'appid': 'c6f729e309025998189cf0eae9dcf9b7',
            'units': 'metric', 
            'lang': 'ru'
            }

    res = requests.get(url, params=payload)
    if res.status_code == 200:
        data = res.json()
        print(f'Текущая температура в городе {data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}')

    else:
        print(f'Не удалось получить информацию о погоде. Код ошибки: {res.status_code}')

get_wether('')
