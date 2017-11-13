from .models import CableStretch, CableStretchType
from .models import Tubeloose
from rest_framework import serializers


class CableStretchTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableStretchType
        fields = [
            'id',
            'description',
        ]


class CableStretchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableStretch
        fields = [
            'id',
            'cod',
            'length',
            'manufacturing_year',
            'infrastructure',
            'owner',
            'fabricant',
            'cable_stretch_type',
            'god_id',
            'segment_id',
            'access_cable_id',
            'access',
            'creation_date',
            'updated_date',
        ]


class TubelooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tubeloose
        fields = [
            'number',
            'stretch_id',
        ]
