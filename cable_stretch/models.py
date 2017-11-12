from django.db import models
from django.utils import timezone
# from dgo.models import GOD


# Create your models here.
class CableStretchType(models.Model):
    description = models.CharField(max_length=30)


class CableStretch(models.Model):
    cod = models.CharField(max_length=20)
    length = models.FloatField(null=True)
    manufacturing_year = models.IntegerField(null=True,default=0)
    infrastructure = models.CharField(null=True,max_length=100)
    owner = models.CharField(null=True,max_length=100)
    fabricant = models.CharField(null=True,max_length=100)
    cable_stretch_type = models.ForeignKey(CableStretchType, null=True)
    access = models.NullBooleanField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
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
