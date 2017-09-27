from rest_framework import serializers
from .models import Uplink


class UplinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uplink
        fields = [
            'id',
            'name_vlan',
            'band',
            'code',
        ]
