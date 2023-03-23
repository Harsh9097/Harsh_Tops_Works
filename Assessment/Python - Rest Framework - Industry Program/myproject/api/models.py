from django.db import models

# Create your models here.
class Studnet(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=50)