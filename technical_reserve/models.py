# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class TechnicalReserve(models.Model):
    code = models.IntegerField(null=False, default=0, unique=True)
    length = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
