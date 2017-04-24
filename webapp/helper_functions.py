import datetime
import requests

weekdays = {'sun', 'mon,tue', 'wed', 'thu', 'fri', 'sat'}
# helper function for clculating the previous year etc


def calculate(year, month):
    """
    Return prev year and prev month etc
    parameters year and month provided by arguments
    this function simply calculate the prev and next month

    """
    if month == 1:
        prev_year = year - 1
        prev_month = 12
        nex_year = year
        nex_month = month + 1
    elif month == 12:
        prev_year = year
        prev_month = month - 1
        nex_year = year + 1
        nex_month = 1
    else:
        prev_year = year
        prev_month = month - 1
        nex_year = year
        nex_month = month + 1
    return prev_year, prev_month, nex_year, nex_month


def add_class(month_calendar, date, month, year):
    """
    Returns a list with a class added to current date
    parameter taken is a tuple
    """
    print date, month, year
    counter_week = 0
    counter_day = 0
    time = datetime.datetime.now()
    if time.month == month and time.year == year:
        for week in month_calendar:
            print counter_day
            for day in week:
                if day == int(date):
                    month_calendar[counter_week][counter_day] = "<span class='active'>" + \
                        str(day) + "</span>"
                counter_day += 1
            counter_day = 0
            counter_week += 1
    return month_calendar


def event_button(dataobject):
    """
    Returns a dictionary containing all the details of all events
    a query dataobject is passed over here
    This data is used to add buttons in the html hence name is event_button
    """

    events = []    # the obtained data will be in the form of tuple so after algo this data will
    # be added to event with proper format
    counter = 0
    for data in dataobject:
        for i in range(int(data.date_begin), int(data.date_end) + 1):
            events.append([int(i), int(data.id)])

    return events


def weather():
    """Returns a string containig temperature"""
    #api url below
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&' + \
        '&APPID=859be65552efd872c991bbfaea55b9d5'
    response = requests.get(url)
    response_json = response.json()
    temperature = response_json['main']['temp']
    #obtaining the json object
    temperature_unit = 'F'
    conditions = response_json['weather'][0]['description']
    return temperature, temperature_unit, conditions
