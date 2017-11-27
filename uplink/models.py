from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Uplink(models.Model):
    name_vlan = models.CharField(blank=False, max_length=50)
    band = models.FloatField(blank=True)
    code = models.IntegerField(blank=False, validators=[MinValueValidator(0)],
                               unique=True)


class Segments(models.Model):
    number = models.IntegerField(blank=True)
    length = models.FloatField(default=0)
