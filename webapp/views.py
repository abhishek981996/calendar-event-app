import calendar
import datetime
from itertools import groupby
from webapp.models import Events
from django.http import HttpResponse
from django.shortcuts import render


def calendars(request, year, month):
    tc = calendar.HTMLCalendar()
    str = tc.formatmonth(int(year), int(month))
    prev_year = int(year)
    prev_month = int(month) - 1
    nex_year = int(year)
    nex_month = int(month) + 1
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
    prev_year = time.year
    prev_month = time.month - 1
    nex_year = time.year
    nex_month = time.month + 1
    return render(request, 'home.html', {
        'htmlCalendar': str,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'nex_year': nex_year,
        'nex_month': nex_month
    })
