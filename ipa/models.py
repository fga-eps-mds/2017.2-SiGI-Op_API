from django.db import models

# Create your models here.

class InstitutionType(models.Model):
    id_type = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

class ParticipantInstitution(models.Model):
    id_ipa = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    institution_type = models.ForeignKey(InstitutionType, null=False)

