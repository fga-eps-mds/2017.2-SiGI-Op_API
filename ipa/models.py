from django.db import models
from django.core.validators import EmailValidator
# Create your models here.


class InstitutionType(models.Model):
    description = models.CharField(max_length=200, null=False)


class ParticipantInstitution(models.Model):
    name = models.CharField(max_length=255, null=False)
    institution_type = models.ForeignKey(InstitutionType, null=False)
    cnpj = models.CharField(blank=True, null=True, max_length=100)
    sigla = models.CharField(blank=True, null=True, max_length=20)


class SiteType(models.Model):
    description = models.CharField(blank=True, max_length=20)


class Event(models.Model):
    ipa_code = models.ForeignKey(InstitutionType, null=False)
    description = models.CharField(null=False, max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    lattitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    City = models.CharField(max_length=300, null=True, blank=True)
    State = models.CharField(max_length=2, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)


class Site(models.Model):
    name = models.CharField(blank=True, max_length=100)
    lattitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    bandwidth = models.PositiveIntegerField(blank=True)
    ipa_code = models.ForeignKey(ParticipantInstitution, null=False)
    site_type = models.ForeignKey(SiteType, null=False)


class ContactType(models.Model):
    description = models.CharField(max_length=40)


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_validator = EmailValidator()
    email = models.CharField(
        validators=[email_validator],
        max_length=40,
        blank=True,
        null=True)
    priority = models.IntegerField(blank=True, null=True)
    contact_type = models.ForeignKey(ContactType, null=False)
    ipa_code = models.ForeignKey(ParticipantInstitution, null=False)


class Generator(models.Model):
    power = models.FloatField(blank=True)
    manufacturer = models.CharField(max_length=50, blank=True)
    patrimony = models.CharField(max_length=20, blank=True, unique=True)
    site = models.ForeignKey(Site, null=False)


class NoBreak(models.Model):
    power = models.FloatField(max_length=6, null=False)
    proprietary = models.CharField(max_length=50, blank=True)
    patrimony_number = models.CharField(max_length=20,
                                        blank=True,
                                        unique=True)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)


class Switch(models.Model):
    serial_number = models.CharField(max_length=30, blank=True, unique=True)
    manufacturer = models.CharField(max_length=30, blank=True)
    slots_quantity = models.PositiveIntegerField(blank=True)
    patrimony_number = models.CharField(max_length=30, blank=True, unique=True)
    site_id = models.ForeignKey(Site, null=False)


class Slot(models.Model):
    serie = models.CharField(max_length=50, blank=True)
    number = models.IntegerField(blank=True)
    patrimony = models.CharField(max_length=30)
    band = models.CharField(max_length=20)
    slot_port_quantity = models.IntegerField(null=False)
    switch_id = models.ForeignKey(Switch, null=False)

    def save(self, **kwargs):  # pylint: disable=arguments-differ
        super(Slot, self).save(**kwargs)
        for _ in range(self.slot_port_quantity):
            slot_port = SlotPort(slot_id=self)
            slot_port.save()


class SlotPort(models.Model):
    port_type = models.CharField(max_length=10)
    port = models.CharField(max_length=50, null=False)
    slot_id = models.ForeignKey(Slot, null=False)
