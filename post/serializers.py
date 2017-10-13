from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'cable_length',
            'stretch',
            'emendation_box',
            'god',
        ]
