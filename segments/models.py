from django.db import models


# Create your models here.
class Segment(models.Model):
    cable_length = models.FloatField()
    segment_number = models.IntegerField()
