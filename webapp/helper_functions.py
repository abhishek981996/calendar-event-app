


weekdays = {'sun','mon,tue','wed','thu','fri','sat'}
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

def add_class(month_calendar,date):
    """
    Returns a list with a class added to current date
    parameter taken is a tuple
    """
    counter_week = 0
    counter_day = 0
    for week in month_calendar:
        for day in week:
            if day == int(date):
                month_calendar[counter_week][counter_day] = "<b class='active'> " 
                                                        + str(day)
                                                        +"</b>"
            counter_day += counter_day
        counter_day = 0
        counter_week +=counter_week

    return month_calendar





