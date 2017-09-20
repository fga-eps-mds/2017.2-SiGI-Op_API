from ipa.models import InstitutionType, ParticipantInstitution
from rest_framework import serializers



class ParticipantInstitutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionType
        fields = [
            'id',
            'description',
        ]

class ParticipantInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantInstitution
        institution_type = ParticipantInstitutionTypeSerializer(many=True, read_only=True)
        fields = [
            'id',
            'name',
            'institution_type',
        ]
