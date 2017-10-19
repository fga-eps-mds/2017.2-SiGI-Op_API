from django.db import models


# Create your models here.
class CableStretch(models.Model):
    length = models.FloatField(blank=False)
    manufacturing_year = models.IntegerField(default=0)
    infrastructure = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    fabricant = models.CharField(max_length=100)
    # segmento
    access = models.BooleanField(blank=False)
    creation_date = models.DateField(blank=False)
    extinction_date = models.DateField(null=True)
