from .models import EmendationBoxStructure, EmendationBoxType, EmendationBox
from rest_framework import serializers


class EmendationBoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmendationBoxType
        fields = [
            'id',
            'description',
        ]


class EmendationBoxStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmendationBoxStructure
        fields = [
            'id',
            'description',
        ]


class EmendationBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmendationBox
        emendation_type = EmendationBoxTypeSerializer(many=True,
                                                      read_only=True)
        emendation_structure = EmendationBoxStructureSerializer(many=True,
                                                                read_only=True)
        fields = [
            'id',
            'lattitude',
            'longitude',
            'designNumber',
            'access_box',
            'creation_date',
            'extinction_date',
            'emendation_type',
            'emendation_structure',
        ]
