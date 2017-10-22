from .models import CableStretch
from .models import Tubeloose
from rest_framework import serializers


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
