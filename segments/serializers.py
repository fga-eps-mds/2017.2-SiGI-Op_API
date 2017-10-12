from .models import Segment
from rest_framework import serializers


class Segments_serializer_class(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = [
            'id',
            'cable_length',
            'segment_number',
        ]
