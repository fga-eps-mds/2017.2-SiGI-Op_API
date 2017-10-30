from django.db import models
# from dgo.models import GOD


# Create your models here.
class CableStretchType(models.Model):
    description = models.CharField(max_length=30)


class CableStretch(models.Model):
    length = models.FloatField(blank=False)
    manufacturing_year = models.IntegerField(default=0)
    infrastructure = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    fabricant = models.CharField(max_length=100)
    cable_stretch_type = models.ForeignKey(CableStretchType, null=False)
    access = models.BooleanField(blank=False)
    creation_date = models.DateField(blank=False)
    updated_date = models.DateField(null=True)
    # dgo some pk issue to solve
    # segment
    # access cable


class Tubeloose(models.Model):
    number = models.IntegerField(blank=False)
    stretch_id = models.ForeignKey(CableStretch, null=False)
