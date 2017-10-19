from django.db import models
from gbic.models import GBIC
from ipa.models import Site

# Create your models here.


class GOD(models.Model):
    code = models.IntegerField(default=0)
    fabricant = models.CharField(max_length=50)
    port_quantity = models.IntegerField(default=1)
    site_id = models.ForeignKey(Site, null=False)


class GODPortConnectionType(models.Model):
    code = models.CharField(blank=False, max_length=50)


class GODPort(models.Model):
    code = models.CharField(blank=False, max_length=50)
    connection_type = models.ForeignKey(GODPortConnectionType)
    god_id = models.ForeignKey(GOD, null=False)
    gbic_id = models.ForeignKey(GBIC, null=False)


class Jumper(models.Model):
    god_port1 = models.ForeignKey(GODPort, null=False, related_name="godport1")
    god_port2 = models.ForeignKey(GODPort, null=False, related_name="godport2")
