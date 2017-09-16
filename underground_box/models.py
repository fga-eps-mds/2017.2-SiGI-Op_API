from django.db import models
from django.utils import timezone

class UndergroundBox(models.Model):
    box_id = models.IntegerField(blank = False)
    box_type = models.CharField(blank = False,max_length = 100)
    latitude = models.FloatField(blank = False)
    cover_type = models.CharField(max_length=100,blank = False)
    longitude = models.FloatField(blank = False)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    removed_at = models.DateTimeField(default=timezone.now, blank=True)
    draw_number = models.IntegerField(blank = False)
