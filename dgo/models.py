from django.db import models

# Create your models here.
class GOD(models.Model):
    code = models.IntegerField(default=0)
    fabricant = models.CharField(max_length=50)
    port_quantity = models.IntegerField(default=1)
