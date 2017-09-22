from .models import GOD
from rest_framework import serializers


class GODSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOD
        fields = [
            'code',
            'fabricant',
            'port_quantity',
        ]
