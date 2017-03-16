# from datetime import date
from django.db import models
# from django.utils import timezone

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date_visited = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def set_date_visited(self, date):
        self.date_visited = date
        self.visited = True

    def __str__(self):
        return self.name

