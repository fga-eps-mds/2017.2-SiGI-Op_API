# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from underground_box import models as underground_models

# Create your models here.

class TechnicalReserve(models.Model):
    length = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    infrastructure = models.ForeignKey(underground_models.UndergroundBox)
