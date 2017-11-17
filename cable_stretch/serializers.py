from rest_framework import serializers
from .models import CableStretch, CableStretchType
from .models import Tubeloose


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
            'length',
            'manufacturing_year',
            'infrastructure',
            'owner',
            'fabricant',
            'cable_stretch_type',
            # segmento
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
