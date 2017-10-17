from django.db import models
# import port_slot

# Create your models here.


class GBIC_Type(models.Model):
    description = models.CharField(max_length=10, blank=False)


class GBIC(models.Model):
    serial = models.CharField(max_length=30, blank=False)
    patrimony_number = models.CharField(max_length=30)
    gbic_type = models.ForeignKey(GBIC_Type)
    # slot_port = models.ForeignKey(Slot_Port, blank=False)
