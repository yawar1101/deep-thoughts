from django.db import models
from django.contrib.auth.models import User


# Event Model

class Event(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    schedule = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='attended_events')


    def __str__(self):
        return self.name




