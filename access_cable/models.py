from django.db import models
from dgo.models import GOD
from ipa.models import Site

# Create your models here.

class AccessCable(models.Model):
    god_id = models.ForeignKey(GOD, null=False)
    site_id = models.ForeignKey(Site, null=False)
    length = models.FloatField(blank=False)
    fiber_quantity = models.IntegerField()
    cod = models.CharField(null=False, max_length=50)
