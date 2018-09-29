# -*- coding: utf-8 -*-
"""
Intro: web scraping
Ref: https://www.dataquest.io/blog/web-scraping-tutorial-python/

"""

# full webscrape, parse into dataframe, & analysis ###

import requests
from bs4 import BeautifulSoup as bs
import re  # regex

# get page
mypage = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
mypage.status_code  # 200 means d/l successful

# parse into beautifulsoup object
soup = bs(mypage.content, 'html.parser')
print(soup.prettify())

# get all links
for link in soup.find_all('a'):
    print(link.get('href')) # hastag means link within page

# finding tags
soup.find_all('p')
soup.find_all('title')
soup.find_all('a')

# using regex within the soup
soup.find_all(re.compile("(^a$|div)"))



# Weather Data Example ###
# scraping from: https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W3hR3OhKhhE

# download webpage
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W3hR3OhKhhE")  # requests.models.Response

# create beautifulsoup class to parse webpage
soup = bs(page.content, 'html.parser')  # bs4.BeautifulSoup

# find the div with the 7 day forecast
seven_day = soup.find(id="seven-day-forecast")  # bs4.element.Tag

# find each individual forecast within the 7 day forecast div
forecast_items = seven_day.find_all(class_="tombstone-container")  # bs4.element.ResultSet

# extract & print first forecast item
tonight = forecast_items[0]  # bs4.element.Tag
print(tonight.prettify())  # string

# extract & print individual information from forecast item
period = tonight.find(class_="period-name").get_text()  # string
short_desc = tonight.find(class_="short-desc").get_text()  # string
temp = tonight.find(class_="temp").get_text()  # string
print(period)
print(short_desc)
print(temp)

# extract title
img = tonight.find('img')  #bs4.element.Tag
desc = img['title']  # string. attribute as key
print(desc)

# select all items with class 'period-name' nested inside items of class 'tombstone-container'
period_tags = seven_day.select(".tombstone-container .period-name")  # list. each element bs4.element.Tag
periods = [pt.get_text() for pt in period_tags]  # list comprehension, call get_text() on each object
periods

# get each short description inside 'tombstone-container'
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]  # list
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]  # list
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]  # string

print(short_descs)
print(temps)
print(descs)

# combine extracted data (mostly in lists) into a single dataframe
import pandas as pd
weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
    })
weather

# regex extract temperatures & create numeric calculated column
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums

# analysis
weather['temp_num'].mean()

# create text calculated column
weather['night time'] = weather['period'].str.contains("night", case=False)

