from django.db import models
# from dgo.models import GOD


# Create your models here.
class CableStretchType(models.Model):
    description = models.CharField(max_length=30)


class CableStretch(models.Model):
    cod = models.CharField(max_length=20)
    length = models.FloatField(null=True)
    manufacturing_year = models.IntegerField(null=True,default=0)
    infrastructure = models.CharField(null=True,max_length=100)
    owner = models.CharField(null=True,max_length=100)
    fabricant = models.CharField(null=True,max_length=100)
    cable_stretch_type = models.ForeignKey(CableStretchType, null=True)
    access = models.NullBooleanField()
    creation_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)
    # dgo some pk issue to solve
    # segment
    # access cable


class Tubeloose(models.Model):
    number = models.IntegerField(blank=False)
    stretch_id = models.ForeignKey(CableStretch, null=False)
