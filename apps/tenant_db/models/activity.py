from django.db import models
from .contact import Contact

activity_codes = {
    'ATTENDANCE': [],
    'FORECASTED ATTENDANCE': ['Y', 'M', 'N'],
    'CALL': ['TODO', 'DNC', 'N/A', 'MSG', 'N/A'],
    'EMAIL': [],
    'KNOCK': [],
    'FLYER': [],
    'SECOND VISIT': []
}


class Activity(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    code = models.CharField(
        max_length=30
    )

    status = models.CharField(
        max_length=30
    )

    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
