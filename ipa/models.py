from django.db import models

# Create your models here.


class SiteType(models.Model):
    description = models.CharField(blank=False, max_length=20)


class Site(models.Model):
    name = models.CharField(blank=False, max_length=100)
    lattitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    bandwidth = models.PositiveIntegerField(blank=False)
    ipa_code = models.IntegerField(blank=False)
    # when get IPA Use case, change this to foreign key
    site_type = models.ForeignKey(SiteType, null=False)
