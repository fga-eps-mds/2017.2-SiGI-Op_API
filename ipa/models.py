from django.db import models
from django.core.validators import EmailValidator
# Create your models here.


class InstitutionType(models.Model):
    description = models.CharField(max_length=200, null=False)


class ParticipantInstitution(models.Model):
    name = models.CharField(max_length=255, null=False)
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
    priority = models.IntegerField(blank=False)
    contact_type = models.ForeignKey(ContactType, null=False)
    ipa_code = models.ForeignKey(ParticipantInstitution, null=False)


class Generator(models.Model):
    power = models.FloatField(blank=False)
    manufacturer = models.CharField(max_length=50, blank=False)
    patrimony = models.CharField(max_length=20, blank=False, unique=True)
    site = models.ForeignKey(Site, null=False)


class NoBreak(models.Model):
    power = models.FloatField(max_length=6, null=False)
    proprietary = models.CharField(max_length=50, null=False)
    patrimony_number = models.CharField(max_length=20, null=False, unique=True)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)


class Switch(models.Model):
    serial_number = models.CharField(max_length=30, null=False, unique=True)
    manufacturer = models.CharField(max_length=30, null=False)
    slots_quantity = models.PositiveIntegerField(blank=False)
    patrimony_number = models.CharField(max_length=30, null=False, unique=True)
    site_id = models.ForeignKey(Site, null=False)


class Slot(models.Model):
    serie = models.CharField(max_length=50, null=False)
    number = models.IntegerField(blank=False)
    patrimony = models.CharField(max_length=30)
    port_quantity = models.IntegerField()
    band = models.CharField(max_length=20)
    switch_id = models.ForeignKey(Switch, null=False)


class SlotPort(models.Model):
    type = models.CharField(max_length=10)
    port = models.CharField(max_length=50, null=False)
    slot_id = models.ForeignKey(Slot, null=False)
