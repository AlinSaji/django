from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    gstin = models.CharField(max_length=225)
    email = models.EmailField()