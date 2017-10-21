from .models import GOD, GODPort, GODPortConnectionType, Jumper
from rest_framework import serializers


class GODSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOD
        fields = [
            'code',
            'fabricant',
            'port_quantity',
        ]


class GODPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GODPort
        fields = [
            'id',
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


class JumperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jumper
        fields = [
            'id',
            'god_port1',
            'god_port2',
        ]
