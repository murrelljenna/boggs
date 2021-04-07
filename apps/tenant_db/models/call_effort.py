from django.db import models
from .activity import Activity


class CallEffort(models.Model):
    name = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CallEffortActivity(models.Model):
    call_effort = models.ForeignKey(CallEffort, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
