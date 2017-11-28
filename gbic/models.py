from django.db import models
# import port_slot

# Create your models here.


class GBICType(models.Model):
    description = models.CharField(max_length=10, blank=False)


class GBIC(models.Model):
    serial = models.CharField(max_length=30, blank=True, unique=True)
    patrimony_number = models.CharField(max_length=30, unique=True)
    gbic_type = models.ForeignKey(GBICType)
    # slot_port = models.ForeignKey(Slot_Port, blank=False)
