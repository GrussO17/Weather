with open('today.txt', 'w') as thing:
    thing.write('this is a file that doesnt do much')
import requests
url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/2089935?apikey=x63orCVKc1eov6PuB4tqZNh0dFIkz4Bz"
day1 = requests.request('GET', url).json()
forecasts = day1.get("DailyForecasts")[0]
date = str(day1.get('Headline').get('EffectiveDate'))
date = date[5:10]
high = int(forecasts.get("Temperature").get("Maximum").get("Value"))
low = int(forecasts.get("Temperature").get("Minimum").get("Value"))
info = str(forecasts.get("Day").get('IconPhrase'))
future = str(day1.get('Headline').get('Text'))
weather = date + ", " + info + "\nHigh of " + str(high) + ", Low of " + str(low) + "\n" + future
"10-25, Mostly cloudy with a High of 67, Low 55. Much cooler tomorrow"
with open('weather.txt', 'w') as thing:
    thing.write(weather)
