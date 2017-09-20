from django.db import models
from django.core.validators import RegexValidator, EmailValidator

# Create your models here.


class ContactType(models.Model):
    name = models.CharField(max_length=40)


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{8,15}$',
        message="""Phone number must be entered in the format: '+999999999'."""
        )
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    email_validator = EmailValidator()
    email = models.CharField(validators=[email_validator], max_length=40)
    priority = models.IntegerField()
    contact_type = models.ForeignKey(
                                ContactType,
                                related_name='contact_type',
                                null=False,
                                default=None)
