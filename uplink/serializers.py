from rest_framework import serializers
from .models import Uplink
from .models import Segments
from dgo.serializers import GODSerializer
from emendation_box.serializers import EmendationBoxSerializer


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
    #dgo = GODSerializer()
    #emendation_box = EmendationBoxSerializer()
    class Meta:
        model = Segments
        fields = [
            'id',
            'number',
            'length',
            'dgos',
            'emendation_boxes',
        ]
