from django.db import models
from gbic.models import GBIC  # <--- Consertar

# Create your models here.


class GOD(models.Model):
    code = models.IntegerField(default=0, unique=True)
    fabricant = models.CharField(max_length=50)
    port_quantity = models.IntegerField(default=1)


class GODPortConnectionType(models.Model):
    code = models.CharField(blank=False, max_length=50)


class GODPort(models.Model):
    code = models.CharField(blank=False, max_length=50)
    connection_type = models.ForeignKey(GODPortConnectionType)
    god_id = models.ForeignKey(GOD, null=False)
    gbic_id = models.ForeignKey(GBIC, null=True)


class Jumper(models.Model):
    god_port1 = models.ForeignKey(GODPort, null=False, related_name="godport1")
    god_port2 = models.ForeignKey(GODPort, null=False, related_name="godport2")
