from .models import Segment
from rest_framework import serializers


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = [
            'cableLength',
            'dgo',
        ]
