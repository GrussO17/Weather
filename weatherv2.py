import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/today/l/ca17339453378200a34be6f36232af711ad68860273bc6c6358dcb731ea0ace6"
response = requests.get(url)


def checkHref(tag):
    if tag.name == 'a' and tag.href == '':
        return True
    return False

soup = BeautifulSoup(response.text, 'html.parser')

better_string_5_day = "The 5 day weather report is:\n"
better_string_today = "Todays weather is"
day_5 = soup.select_one('div[class*="DailyWeatherCard--TableWrapper--"]')
each_day = day_5.select('li[class*="Column--column"]')
for day in each_day:
    better_string_5_day += day.select_one('h3[class*="Column--label"]').text + " -- "
    better_string_5_day += "High: " + day.find('div', {"data-testid": "SegmentHighTemp"}).text[:-1] + " Low: " + day.find('div', {"data-testid": "SegmentLowTemp"}).text[:-1] + "\n"
    better_string_5_day += "Precipitation chance: " + day.find('div', {"data-testid": "SegmentPrecipPercentage"}).text + "\n\n"

today = soup.select_one('div[id*="WxuTodayWeatherCard"]')
today_sectors = today.select('a[class*="Column--innerWrapper"]')


print(better_string_5_day)

with open('day5.txt', 'w') as thing:
    thing.write(better_string_5_day)


