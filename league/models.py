from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class League(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name', unique=True)
    users = models.ManyToManyField(User, through="Profile", related_name="leagues")

class Game(models.Model):
    agent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="agent")
    patient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="patient")
    league = models.ForeignKey(League, null=True, on_delete=models.CASCADE, related_name="games")
    timestamp = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.agent.username + " vs. " + self.patient.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="profiles")
    packs_claimed = models.IntegerField(default=0)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "league"], name="unique_user_league"
            )
        ]