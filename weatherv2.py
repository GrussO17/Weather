import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/today/l/ca17339453378200a34be6f36232af711ad68860273bc6c6358dcb731ea0ace6"
response = requests.get(url)


def checkHref(tag):
    if tag.name == 'a' and tag.href == '':
        return True
    return False

soup = BeautifulSoup(response.text, 'html.parser')
times_in_a_day = ['Morning  ', 'Afternoon', 'Evening  ', 'Overnight']

better_string_5_day = "The 5 day weather report is:\n"
better_string_today = "Today's weather\n"

skycodes = {
    '0': 'Thunderstorm',
    '1': 'Thunderstorm',
    '2': 'Thunderstorm',
    '3': 'Thunderstorm',
    '4': 'Thunderstorm',
    '17': 'Thunderstorm',
    '5': 'Snow and Rain',
    '6': 'Snow and Sleet',
    '7': 'Rain, Snow and Sleet',
    '8': 'Icy',
    '9': 'Icy',
    '10': 'Rain and Sleet',
    '11': 'Light rain',
    '12': 'Rain',
    '13': 'Light Snow',
    '14': 'Snow',
    '16': 'Snow',
    '42': 'Snow',
    '43': 'Snow',
    '15': 'Blizzard',
    '18': 'Showers',
    '40': 'Showers',
    '19': 'Dust',
    '20': 'Fog',
    '21': 'Haze',
    '22': 'Smokey',
    '23': 'Windy',
    '24': 'Windy',
    '25': 'Frigid',
    '26': 'Cloudy',
    '27': 'Partly Cloudy',
    '29': 'Partly Cloudy',
    '33': 'Partly Cloudy',
    '28': 'Partly Cloudy',
    '30': 'Partly Cloudy',
    '34': 'Partly Cloudy',
    '31': 'Clear',
    '32': 'Clear',
    '36': 'Hot',
    '37': 'Scattered Thunderstorms',
    '38': 'Scattered Thunderstorms',
    '39': 'Scattered Showers',
    '41': 'Scattered Snow Showers',
    '44': 'IDK',
    '45': 'Scattered Rain Showers',
    '46': 'Scattered Snow Storms',
    '47': 'Scattered Thunderstorms'
}

day_5 = soup.select_one('div[class*="DailyWeatherCard--TableWrapper--"]')
each_day = day_5.select('li[class*="Column--column"]')
for day in each_day:
    better_string_5_day += day.select_one('h3[class*="Column--label"]').text + " -- "
    better_string_5_day += "High: " + day.find('div', {"data-testid": "SegmentHighTemp"}).text[:-1] + " Low: " + day.find('div', {"data-testid": "SegmentLowTemp"}).text[:-1] + "\n"
    better_string_5_day += "Precipitation chance: " + day.find('div', {"data-testid": "SegmentPrecipPercentage"}).text + "\n\n"

today = soup.select_one('div[id*="WxuTodayWeatherCard"]')
today_sectors = today.select('a[class*="Column--innerWrapper"]')

count = 0;
for columns in today_sectors:
    better_string_today += times_in_a_day[count] + ": " + columns.select_one('div[data-testid*=SegmentHighTemp]').text[:-1] + "F Precip: "
    better_string_today += columns.select_one('div[data-testid*=SegmentPrecipPercentage]').text + "  "
    better_string_today += skycodes[columns.find('svg',  {'set': 'weather'})['skycode']] + '\n'
    count += 1


#print(better_string_today)
#print(better_string_5_day)

with open('today.txt', 'w') as today:
    today.write(better_string_today)

with open('day5.txt', 'w') as thing:
    thing.write(better_string_5_day)


