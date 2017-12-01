from rest_framework import serializers
from .models import GBIC, GBICType


class GBICTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GBICType
        fields = [
            'id',
            'description',
        ]


class GBICSerializer(serializers.ModelSerializer):
    class Meta:
        model = GBIC
        fields = [
            'id',
            'serial',
            'patrimony_number',
            'gbic_type',
            # 'slot_port'
        ]
