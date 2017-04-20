import calendar
import datetime
from itertools import groupby
from webapp.models import Events
from django.http import HttpResponse
from django.shortcuts import render


# helper function for clculating the previous year etc
def calculate(year, month):
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


def calendars(request, year, month):
    tc = calendar.HTMLCalendar()
    str = tc.formatmonth(int(year), int(month))
    prev_year, prev_month, nex_year, nex_month = calculate(
        int(year), int(month))
    print '%s,%s,%s,%s' % (prev_year, prev_month, nex_year, nex_month)
    return render(request, 'home.html', {
        'htmlCalendar': str,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'nex_year': nex_year,
        'nex_month': nex_month
    })


def today(request):
    time = datetime.datetime.now()
    tc = calendar.HTMLCalendar()
    str = tc.formatmonth(time.year, time.month)
    prev_year, prev_month, nex_year, nex_month = calculate(
        int(time.year), int(time.month))

    return render(request, 'home.html', {
        'htmlCalendar': str,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'nex_year': nex_year,
        'nex_month': nex_month
    })
