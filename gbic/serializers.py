from .models import GBIC, GBIC_Type
from rest_framework import serializers


class GBIC_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GBIC_Type
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
