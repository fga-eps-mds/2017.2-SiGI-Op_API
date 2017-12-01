from rest_framework import serializers
from .models import Uplink
from .models import Segments


class UplinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uplink
        fields = [
            'id',
            'name_vlan',
            'band',
            'code',
        ]


class SegmentsSerializer(serializers.ModelSerializer):
    slug_field = 'number'

    class Meta:
        model = Segments
        fields = [
            'id',
            'number',
            'length',
            'dgos',
            'emendation_boxes',
        ]
