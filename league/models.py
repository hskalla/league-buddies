from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class League(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name', unique=True)
    users = models.ManyToManyField(User, related_name="leagues")

class Game(models.Model):
    agent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="agent")
    patient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="patient")
    league = models.ForeignKey(League, null=True, on_delete=models.CASCADE, related_name="games")
    timestamp = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField()
    confirmed = models.BooleanField(default=False)