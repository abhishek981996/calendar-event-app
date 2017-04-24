from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
time = datetime.datetime.now()


class EventsDetails(models.Model):
    id = models.IntegerField(primary_key=True)#setting primary key for this model
    event = models.CharField(max_length=50)
    year = models.IntegerField(default=time.year)
    month = models.IntegerField(default=time.month)
    date_begin = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50)
    time_start = models.IntegerField()
    time_ends = models.IntegerField()
    Location = models.CharField(max_length=50)
    Description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '%s, %s, %s, %s,%s ,%s' % (self.id, self.event, self.date_begin, self.date_end,
                                          self.time_start, self.time_ends)
    #so the value returned during quering this model is done by __str__