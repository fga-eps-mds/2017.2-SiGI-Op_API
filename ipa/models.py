from django.db import models
from django.core.validators import EmailValidator

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


class ContactType(models.Model):
    description = models.CharField(max_length=40)


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    email_validator = EmailValidator()
    email = models.CharField(validators=[email_validator], max_length=40)
    priority = models.IntegerField()
    contact_type = models.ForeignKey(ContactType, null=False)
    ipa_code = models.ForeignKey(ParticipantInstitution, null=False)


class Switch(models.Model):
    serial_number = models.CharField(max_length=30, null=False)
    fabricant = models.CharField(max_length=30)
    qtd_slots = models.PositiveIntegerField(blank=False)
    patrimony_number = models.CharField(max_length=30)
    site_id = models.ForeignKey(SiteType, null=False)
