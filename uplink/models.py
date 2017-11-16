from django.db import models
from django.core.validators import MinValueValidator
from dgo.models import GOD
from emendation_box.models import EmendationBox

# Create your models here.
class Uplink(models.Model):
    name_vlan = models.CharField(blank=False, max_length=50)
    band = models.FloatField(blank=False)
    code = models.IntegerField(blank=False, validators=[MinValueValidator(0)],
                               unique=True)


class Segments(models.Model):
    number = models.IntegerField(null=False)
    length = models.FloatField(default=0)
    dgos = models.ManyToManyField(GOD, blank=True)
    emendation_boxes = models.ManyToManyField(EmendationBox, blank=True)
    
