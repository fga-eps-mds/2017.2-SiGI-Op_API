from django.db import models
from dgo.models import GOD


# Create your models here.
class Segment(models.Model):
    cableLength = models.FloatField()
    dgo = models.ForeignKey(GOD, null=False)
