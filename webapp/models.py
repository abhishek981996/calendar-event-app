from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=50)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    time_start = models.IntegerField()
    time_ends = models.IntegerField()
    Location = models.CharField(max_length=50)
    Description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.event, self.year, self.month, self.date)
