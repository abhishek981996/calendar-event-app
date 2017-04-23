# developed by abhishek981996
# all comments are written below the functioning line
# for calendar webapp

import calendar
import datetime
# timezone is different so it may differ for IST
from itertools import groupby
from webapp.models import EventsDetails
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from webapp.helper_functions import calculate, add_class, event_button
# calculate function is used to calculate the prev next month and year
# add_class adds a tag <b> and class active to the given date in a tuple
# add_class is used for adding css for current date
# then we use the jqery to display green color to the current date using
# class active
from webapp.forms import EventForm


month = {'1': 'January',
         '2': 'Febuary',
         '3': 'March',
         '4': 'April',
         '5': 'May',
         '6': 'June',
         '7': 'July',
         '8': 'August',
         '9': 'Sebtember',
         '10': 'Octobar',
         '11': 'November',
         '12': 'December'}
# a dictionary containing month no as key this will be used to
# take month name using the month no, like if time.month wil return 3 which
# I will use as a key in this dictionary to get full name of month


def calendars(request, year, monthe):
    time = datetime.datetime.now()
    month_array = calendar.monthcalendar(int(year), int(monthe))
    prev_year, prev_month, nex_year, nex_month = calculate(
        int(year), int(monthe))

    month_name = month[str(monthe)]
    edited_month_array = add_class(
        month_array, int(time.day), int(monthe), int(year))
    query = EventsDetails.objects.filter(
        month=monthe, year=year)
    EventForm_detail = EventForm()
    events = event_button(query)
    return render(request, 'calendar_table.html', {
        'htmlcalendar': month_array,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'nex_year': nex_year,
        'nex_month': nex_month,
        'month_name': month_name,
        'this_year': year,
        'EventForm': EventForm_detail,
        'events': events,
        'range': range(len(events)),
        'query': query
    })


def today(request):
    time = datetime.datetime.now()
    # getting current time using datetime module
    month_array = calendar.monthcalendar(int(time.year), int(time.month))
    prev_year, prev_month, nex_year, nex_month = calculate(
        int(time.year), int(time.month))
    print time
    month_name = month[str(time.month)]
    # getting present month name
    EventForm_detail = EventForm()
    edited_month_array = add_class(
        month_array, time.day, time.month, time.year)
    # the function for adding active class for current date and weekday starts
    # here
    query = EventsDetails.objects.filter(
        month=time.month, year=time.year)
    events = event_button(query)  # seperating the fromat inorder to
    # use it in template
    return render(request, 'home.html', {
        'month_name': month_name,
        'htmlcalendar': month_array,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'nex_year': nex_year,
        'nex_month': nex_month,
        'this_year': str(time.year),
        'EventForm': EventForm_detail,
        'events': events,
        'range': range(len(events)),
        'query': query
    })


def form_submit(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect(today)
        return HttpResponse("error in form")
    return HttpResponse("sucesss get request")


def view_events(request, id):
    query = EventsDetails.objects.get(
        id=id)
    print query
    return render(request, 'view_event.html', {
        'query': query,
        'id': id, })


def edit_events(request, id):
    query = EventsDetails.objects.get(
        id=id)
    form = EventForm(instance=query)
    return render(request, "edit_event.html", {
        'form': EventForm_detail,
        'id': id,
    })
