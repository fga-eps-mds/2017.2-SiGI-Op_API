from django.db import models

# Create your models here.


class Segments(models.Model):
    number = models.IntegerField(null=False)
    length = models.FloatField(default=0)
