from django.db import models
from dgo.models import GOD


# Create your models here.
class Segment(models.Model):
    cable_length = models.FloatField()
    dgo = models.ForeignKey(GOD, null=False)
