"""
This module manages fields for cable stretch and its type, and Tubelooses.
"""
from django.db import models
from dgo.models import GOD, AccessCable
from uplink.models import Segments

# from dgo.models import GOD


# Create your models here.
class CableStretchType(models.Model):
    """
    This class manages CableStretchType table.
    """
    description = models.CharField(max_length=30)


class CableStretch(models.Model):
    """
    This class manages CableStretch table.
    """
    cod = models.CharField(max_length=20)
    length = models.FloatField(blank=True, null=True)
    manufacturing_year = models.IntegerField(blank=True, null=True, default=0)
    infrastructure = models.CharField(blank=True, null=True, max_length=100)
    owner = models.CharField(blank=True, null=True, max_length=100)
    fabricant = models.CharField(blank=True, null=True, max_length=100)
    cable_stretch_type = models.ForeignKey(CableStretchType,
                                           blank=True,
                                           null=True)
    access = models.NullBooleanField(blank=True, default=False)
    god_id = models.ForeignKey(GOD, null=True, blank=True)
    segment_id = models.ForeignKey(Segments, null=True, blank=True)
    access_cable_id = models.ForeignKey(AccessCable, null=True, blank=True)
    creation_date = models.DateTimeField(null=True,
                                         auto_now_add=True,
                                         blank=True)
    updated_date = models.DateTimeField(null=True, auto_now=True, blank=True)
    # dgo some pk issue to solve
    # access cable


class Tubeloose(models.Model):
    """
    This class manages Tubeloose table.
    """
    number = models.IntegerField(blank=True)
    stretch_id = models.ForeignKey(CableStretch, null=False)
