from rest_framework import serializers
from .models import TechnicalReserve

class TechnicalReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalReserve
        fields = [
            'id',
            'code',
            'length',
            'lattitude',
            'longitude',
        ]
