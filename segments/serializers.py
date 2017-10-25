from .models import Segments
from rest_framework import serializers


class SegmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segments
        fields = [
            'number',
            'length',
        ]
