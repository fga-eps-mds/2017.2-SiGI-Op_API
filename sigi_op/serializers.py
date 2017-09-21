from rest_framework import serializers
from dgo.models import GOD

class GODSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOD
        fields = [
            'code',
            'fabricant',
            'port_quantity',
        ]
