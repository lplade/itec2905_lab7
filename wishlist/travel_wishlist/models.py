from datetime import date
from django.db import models
from django.utils import timezone

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date_visited = models.DateField(default=timezone.now)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
