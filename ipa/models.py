from django.db import models

# Create your models here.

class InstitutionType(models.Model):
    description = models.CharField(max_length=200)

class ParticipantInstitution(models.Model):
    name = models.CharField(max_length=255)
    institution_type = models.ForeignKey(InstitutionType, null=False)

