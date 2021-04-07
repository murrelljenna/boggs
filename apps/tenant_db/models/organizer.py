from django.db import models


class Organizer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
