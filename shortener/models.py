from django.db import models

# Create your models here.
# Models act as database
class Url(models.Model):
    # Url link provided with max char length of 10k
    link = models.CharField(max_length=10000)
    # Shortened Url with char length 10
    uuid = models.CharField(max_length=10)