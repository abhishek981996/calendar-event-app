import datetime

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
