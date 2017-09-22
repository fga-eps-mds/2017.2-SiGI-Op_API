from django.db import models

# Create your models here.


class InstitutionType(models.Model):
    description = models.CharField(max_length=200)


class ParticipantInstitution(models.Model):
    name = models.CharField(max_length=255)
    institution_type = models.ForeignKey(InstitutionType, null=False)


class SiteType(models.Model):
    description = models.CharField(blank=False, max_length=20)


class Site(models.Model):
    name = models.CharField(blank=False, max_length=100)
    lattitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    bandwidth = models.PositiveIntegerField(blank=False)
    ipa_code = models.ForeignKey(ParticipantInstitution, null=False)
    site_type = models.ForeignKey(SiteType, null=False)
