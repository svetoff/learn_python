import datetime
import requests

token = '63f404fe951e9943e1a280777c2718df'
print('Enter your city: ')
city = input()
print('Enter number of days')
days = input()
url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&lang=ru&units=metric&appid=' + token

response = requests.get(url)
j = response.json()

n = 0
while n < int(days):
    udate = j["list"][n]["dt"]
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d-%m-%Y')
    temp_min = j["list"][n]["main"]["temp_min"]
    temp_max = j["list"][n]["main"]["temp_max"]
    weather = j["list"][n]["weather"][0]["description"]
    n += 1
    print(
        "Date: {}\n Min-temp: {}\n Max-temp: {}\n weather: {}\n -=======-".format(date, temp_min, temp_max, weather))

