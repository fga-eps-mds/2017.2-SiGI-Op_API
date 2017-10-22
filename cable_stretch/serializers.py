from .models import CableStretch, CableStretchType
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
