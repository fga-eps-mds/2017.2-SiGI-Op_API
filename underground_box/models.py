from django.db import models
from emendation_box.models import EmendationBox
from technical_reserve.models import TechnicalReserve


class UndergroundBoxType(models.Model):
    name = models.CharField(blank=False, max_length=100)


class UndergroundBox(models.Model):
    code = models.CharField(max_length=200, blank=False, default='none',
                            unique=True)
    box_type = models.ForeignKey(UndergroundBoxType, null=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    cover_type = models.CharField(max_length=20, blank=False)
    emendation_box = models.ForeignKey(EmendationBox, null=False)
    technical_reserve = models.ForeignKey(TechnicalReserve, null=False)
