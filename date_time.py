import datetime
# pip install pytz    allow us to use timezone
import pytz

# get today's date
today_date = datetime.date.today()
# print(today_date)

# birthday
birthday = datetime.date(1991, 4, 24)
# print(birthday)

# how many days I lived since my birth
days_since_birth = (today_date - birthday).days
# print(days_since_birth)

# finding date in 10days
time_delta = datetime.timedelta(days=10)
# print(today_date + time_delta)

# find which day, month, weekdays (monday as 0 and sunday as 6) is it
# print(today_date.day)
# print(today_date.month)
# print(today_date.weekday())

# Time
print(datetime.datetime(2020, 2, 18, 7, 2, 20, 15))
# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)

# add 10 hours to current time
hour_delta = datetime.timedelta(hours=10)
# print(datetime.datetime.now() + hour_delta)

# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568 to check all timezones or
# for tz in pytz.all_timezones:
# print(tz)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
datetime_paris = datetime_today.astimezone(pytz.timezone('Europe/Paris'))
# print(datetime_pacific)
# print(datetime_paris)

# string formatting with dates. %B = month, %d = day, %Y = year  strgtime means formating
# 2019-03-09 -> March 3, 2019
# print(datetime_pacific.strftime('%B %d, %Y'))

# How to go from a datetime to a date object : March 09, 2019 -> datetime(2019,3,9). strptime means parsing
datetime_thing = datetime.datetime.strptime("March 09, 2020", "%B %d, %Y")
print(datetime_thing)

# check https://github.com/timofurrer/maya     for easier date manipulation
