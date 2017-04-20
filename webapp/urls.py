from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<year>\w{4})/(?P<month>\d+)',
        views.calendars, name='calendar'),
    url(r'^$', views.today, name='calendar_now')
]
