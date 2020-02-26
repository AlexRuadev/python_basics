# getting data from a website to store them somewhere

# pip install beautifulsoup4
# pip install requests
# pip install pandas

import pandas as pd
import requests
from bs4 import BeautifulSoup

# make a request to our website
page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999")
# get the html from the page using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

# to get all the <a> elements
# print(soup.find_all("a"))

# get the content from the div with id="seven-day-forecast-body"
week = soup.find(id="seven-day-forecast-body")
# print(week)

# !!!! Don't forget the _ after class when you want to find_all by class
items = week.find_all(class_="tombstone-container")
# to get the first tombstone-container from the html page, select by index.
# print(items[0])

# get the text inside the first tombstone-container, in the div with the class="period-name"
# print(items[0].find(class_="period-name").get_text())

# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

# create a list comprehension to do a for loop to go over each day of the week
# for each item, in items, as you loop through it, find the div with the class period-name, and get the text
period_names = [item.find(class_="period-name").get_text() for item in items]
# print(period_names)
short_descriptions = [
    item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]

# print(period_names)
# print(short_descriptions)
# print(temperatures)

# using pandas to display our data in a table
# DataFrame takes a dictionnary
weather_stuff = pd.DataFrame({
    "period": period_names,
    "short_descriptions": short_descriptions,
    "temperatures": temperatures
})

print(weather_stuff)
# exemple to get one specific data
print(period_names[1] + ' ' + short_descriptions[1] + ' ' + temperatures[1])

# using Pandas fonction .to_csv() to create a csv file with our data.
weather_stuff.to_csv("weather.csv")
