from django.db import models

# Create your models here.


class SiteType(models.Model):
    type_id = models.IntegerField(blank=False)
    name = models.CharField(blank=False, max_length=20)


class Site(models.Model):
    site_id = models.IntegerField(blank=False)
    name = models.CharField(blank=False, max_length=100)
    lattitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    bandwidth = models.IntegerField(blank=False)
    IPa_code = models.IntegerField(blank=False)
    type_site = models.ForeignKey(SiteType, null=False)
