# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from underground_box import models as underground_models

# Create your models here.

class TechnicalReserve(models.Model):
    code = models.IntegerField(null=False, default=0)
    length = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
