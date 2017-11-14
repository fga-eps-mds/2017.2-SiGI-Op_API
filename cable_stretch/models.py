from django.db import models
from django.utils import timezone
from dgo.models import GOD, AccessCable
from uplink.models import Segments

# from dgo.models import GOD


# Create your models here.
class CableStretchType(models.Model):
    description = models.CharField(max_length=30)


class CableStretch(models.Model):
    cod = models.CharField(max_length=20)
    length = models.FloatField(blank=True, null=True)
    manufacturing_year = models.IntegerField(blank=True, null=True, default=0)
    infrastructure = models.CharField(blank=True, null=True, max_length=100)
    owner = models.CharField(blank=True, null=True, max_length=100)
    fabricant = models.CharField(blank=True, null=True, max_length=100)
    cable_stretch_type = models.ForeignKey(CableStretchType,
                                           blank=True,
                                           null=True)
    access = models.NullBooleanField(blank=True)
    god_id = models.ForeignKey(GOD, null=True, blank=True)
    segment_id = models.ForeignKey(Segments, null=True, blank=True)
    access_cable_id = models.ForeignKey(AccessCable, null=True, blank=True)
    creation_date = models.DateTimeField(null=True,
                                         auto_now_add=True,
                                         blank=True)
    updated_date = models.DateTimeField(null=True, auto_now=True, blank=True)
    # dgo some pk issue to solve
    # segment
    # access cable

    def save(self, *args, **kwargs):
        print("Debugging")
        ''' On save, update timestamps '''
        if not self.id:
            self.creation_date = timezone.now()
        self.updated_date = timezone.now()
        return super(CableStretch, self).save(*args, **kwargs)


class Tubeloose(models.Model):
    number = models.IntegerField(blank=False)
    stretch_id = models.ForeignKey(CableStretch, null=False)
