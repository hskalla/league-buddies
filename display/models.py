from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=32)
    invite_code = models.CharField(max_length=64)

class Game(models.Model):
    agent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="agent")
    patient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="patient")
    timestamp = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField()
    confirmed = models.BooleanField(default=False)