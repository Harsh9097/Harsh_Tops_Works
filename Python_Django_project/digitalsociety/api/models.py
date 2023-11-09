from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

