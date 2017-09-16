from rest_framework import serializers
from underground_box.models import UndergroundBox

class UndergroundBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model= UndergroundBox
        fields = ('box_id','box_type','latitude','cover_type','longitude','created_at','removed_at','draw_number')
