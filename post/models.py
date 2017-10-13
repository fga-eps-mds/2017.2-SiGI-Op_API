from django.db import models
from emendation_box.models import EmendationBox
from dgo.models import GOD


# Create your models here.
class Post(models.Model):
    cable_length = models.FloatField(blank=False)
    stretch = models.IntegerField(blank=False)
    emendation_box = models.ForeignKey(EmendationBox, null=False)
    god = models.ForeignKey(GOD, null=False)
