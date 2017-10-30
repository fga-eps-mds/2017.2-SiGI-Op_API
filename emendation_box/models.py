from django.db import models


# Create your models here.
class EmendationBoxStructure(models.Model):
    description = models.CharField(max_length=20, null=False)


class EmendationBoxType(models.Model):
    description = models.CharField(max_length=100, null=False)


class EmendationBox(models.Model):
    lattitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    designNumber = models.IntegerField(blank=False, unique=True)
    access_box = models.BooleanField(blank=False)
    creation_date = models.DateField(blank=False)
    extinction_date = models.DateField(null=True)
    emendation_type = models.ForeignKey(EmendationBoxType, null=False)
    emendation_structure = models.ForeignKey(EmendationBoxStructure,
                                             null=False)
