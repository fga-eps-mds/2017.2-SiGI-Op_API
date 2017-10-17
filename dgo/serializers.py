from .models import GOD, GODPort, GODPortConnectionType
from rest_framework import serializers


class GODSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOD
        fields = [
            'code',
            'fabricant',
            'port_quantity',
            'site_id',
        ]


class GODPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GODPort
        fields = [
            'code',
            'connection_type',
            'god_id',
            'gbic_id',
        ]


class GODPortConnectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GODPortConnectionType
        fields = [
            'code'
        ]
