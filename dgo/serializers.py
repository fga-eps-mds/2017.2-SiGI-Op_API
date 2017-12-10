from ipa.serializers import SiteSerializer
from rest_framework import serializers
from .models import GOD, GODPort, GODPortConnectionType, Jumper, AccessCable
from .models import GODFabricant, GODFabricantModel


class GODFabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GODFabricant
        fields = [
            'id',
            'description',
        ]


class GODFabricantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GODFabricantModel
        fields = [
            'id',
            'fabricant_id',
            'name',
            'port_quantity',
        ]


class GODSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOD
        fields = [
            'id',
            'code',
            'god_model',
            'site_id',
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
            'code',
        ]


class JumperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jumper
        fields = [
            'id',
            'god_port1',
            'god_port2',
        ]


class AccessCableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessCable
        god_id = GODSerializer(many=True, read_only=True)
        site_id = SiteSerializer(many=True, read_only=True)
        fields = [
            'id',
            'length',
            'fiber_quantity',
            'cod',
            'site_id',
            'god_id',
        ]
