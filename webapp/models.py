from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EventsDetails(models.Model):
    event = models.CharField(max_length=50)
    date_begin = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50)
    time_start = models.IntegerField()
    time_ends = models.IntegerField()
    Location = models.CharField(max_length=50)
    Description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '%s, %s, %s, %s,%s' % (self.event, self.date_begin, self.date_end,
                                      self.time_start, self.time_ends)
