from django.db import models
from dgo.models import GOD


# Create your models here.
class EmendationBoxStructure(models.Model):
    description = models.CharField(max_length=20)


class EmendationBoxType(models.Model):
    description = models.CharField(max_length=100)


class EmendationBox(models.Model):
    lattitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    designNumber = models.IntegerField(blank=False)
    access_box = models.BooleanField(blank=False)
    creation_date = models.DateField(blank=False)
    extinction_date = models.DateField(null=True)
    emendation_type = models.ForeignKey(EmendationBoxType, null=False)
    emendation_structure = models.ForeignKey(EmendationBoxStructure,
                                             null=False)


class Post(models.Model):
    cable_length = models.FloatField(blank=False)
    stretch = models.IntegerField(blank=False)
    emendation_box = models.ForeignKey(EmendationBox, null=False)
    god = models.ForeignKey(GOD, null=False)
