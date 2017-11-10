from rest_framework import serializers
from .models import UndergroundBox, UndergroundBoxType
from emendation_box.serializers import EmendationBoxSerializer
from technical_reserve.serializers import TechnicalReserveSerializer


class UndergroundBoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergroundBoxType
        fields = [
            'id',
            'name',
        ]


class UndergroundBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergroundBox
        box_type = UndergroundBoxTypeSerializer(many=True, read_only=True)
        emendation_box = EmendationBoxSerializer(many=True, read_only=True)
        technical_reserve = TechnicalReserveSerializer(many=True,
                                                       read_only=True)
        fields = [
                'id',
                'code',
                'box_type',
                'lattitude',
                'longitude',
                'cover_type',
                'emendation_box',
                'technical_reserve',
        ]
