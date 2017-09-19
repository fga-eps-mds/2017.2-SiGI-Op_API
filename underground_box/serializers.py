from rest_framework import serializers
from underground_box.models import UndergroundBox, UndergroundBoxType


class UndergroundBoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergroundBoxType
        fields = [
            'type_id',
            'name',
        ]


class UndergroundBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergroundBox
        box_type = UndergroundBoxTypeSerializer(many=True, read_only=True)
        fields = [
                'box_id',
                'box_type',
                'latitude',
                'cover_type',
                'longitude',
                'created_at',
                'removed_at',
                'draw_number',
        ]
