"""
This module manages the serialization of the CableStretchType,
CableStretch and Tubeloose objects.
"""
from rest_framework import serializers
from .models import CableStretch, CableStretchType
from .models import Tubeloose
from .models import Post


class CableStretchTypeSerializer(serializers.ModelSerializer):
    """
    This class manages the serialization of the CableStretchType objects.
    """
    class Meta(object):
        """
        This class manages the metadata of CableStretch.
        """
        model = CableStretchType
        fields = [
            'id',
            'description',
        ]


class CableStretchSerializer(serializers.ModelSerializer):
    """
    This class manages the serialization of the CableStretch objects.
    """
    class Meta(object):
        """
        This class manages the metadata of CableStretch.
        """
        model = CableStretch
        fields = [
            'id',
            'cod',
            'length',
            'manufacturing_year',
            'infrastructure',
            'owner',
            'fabricant',
            'cable_stretch_type',
            'god_id',
            'segment_id',
            'access_cable_id',
            'access',
            'creation_date',
            'updated_date',
        ]


class TubelooseSerializer(serializers.ModelSerializer):
    """
    This class manages the serialization of the Tubeloose objects.
    """
    class Meta(object):
        """
        This class manages the metadata of Tubeloose.
        """
        model = Tubeloose
        fields = [
            'id',
            'number',
            'stretch_id',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'cable_length',
            'cable_stretch',
            'emendation_box',
            'god',
        ]
