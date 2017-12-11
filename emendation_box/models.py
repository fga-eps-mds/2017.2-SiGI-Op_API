from django.db import models


# Create your models here.
class EmendationBoxStructure(models.Model):
    description = models.CharField(max_length=20, null=False)


class EmendationBoxType(models.Model):
    description = models.CharField(max_length=100, null=False)


class EmendationBox(models.Model):
    lattitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    designNumber = models.IntegerField(blank=True, unique=True)
    access_box = models.BooleanField(blank=True, default=False)
    creation_date = models.DateField(blank=False, auto_now_add=True)
    extinction_date = models.DateField(null=True)
    emendation_type = models.ForeignKey(EmendationBoxType, null=False)
    emendation_structure = models.ForeignKey(EmendationBoxStructure,
                                             null=False)
