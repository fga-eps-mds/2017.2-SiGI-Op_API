from django.db import models
from django.core.validators import MinValueValidator
from dgo.models import GOD
from emendation_box.models import EmendationBox


class Uplink(models.Model):
    name_vlan = models.CharField(blank=False, max_length=50)
    band = models.FloatField(blank=True)
    code = models.IntegerField(blank=False, validators=[MinValueValidator(0)],
                               unique=True)


class Segments(models.Model):
    number = models.IntegerField(blank=True)
    length = models.FloatField(default=0)
    dgos = models.ManyToManyField(GOD, null=True, blank=True)
    emendation_boxes = models.ManyToManyField(
        EmendationBox,
        null=True,
        blank=True
        )


class GODSegment(models.Model):
    segments_id = Segments()
    god_id = GOD()


class EmendationBoxSegment(models.Model):
    segments_id = Segments()
    emendationbox_id = EmendationBox()
