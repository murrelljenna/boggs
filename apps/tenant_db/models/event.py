from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
