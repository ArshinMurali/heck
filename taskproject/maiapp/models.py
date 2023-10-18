from django.db import models

# Create your models here.
class Main(models.Model):
    one = models.CharField(max_length=250)
    two = models.CharField(max_length=250)
    three = models.CharField(max_length=250)