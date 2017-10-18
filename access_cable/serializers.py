from .models import AccessCable
from rest_framework import serializers

class AccessCableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessCable
        fields = [
            'god_id'
            'site_id'
            'lenght'
            'fiber_quantity'
            'cod'
        ]
