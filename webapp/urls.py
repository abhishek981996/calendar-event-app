from django.conf.urls import url, include
from . import views
# importing all the views from webapp.views file

urlpatterns = [
    url(r'^(?P<year>\w{4})/(?P<monthe>\d+)',
        views.calendars, name='calendar'),
    # when the user clicks on prev month or prev year then this url is called
    # it takes 2 parameter
    # 1) year 2) month for detecting whether he she wants prev or
    # next_month

    url(r'^$', views.today, name='calendar_now'),
    # when the user opens this webapp he/she will see this calendar_now
    # from the above url. It simply displays the calendar with today date and
    # month
    url(r'^form-submit/', views.form_submit, name='form_submit'),
    # here in this url we will just use the parameter to display the data of that
    # event this data will then be used by ajax call to display a simple modal
    # window.This help from creating more than one modal window in one page
    # and populating them
    url(r'^view-events/(?P<id>\d+)',
        views.view_events, name="view_events"),
    url(r'^edit-events/(?P<id>\d+)', views.edit_events, name="edit_events")
]
