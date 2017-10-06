from .models import InstitutionType, ParticipantInstitution, ContactType, Generator
from .models import Contact
from sigi_op.serializers import SiteSerializer
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
        institution_type = ParticipantInstitutionTypeSerializer(many=True,
                                                                read_only=True)
        fields = [
            'id',
            'name',
            'institution_type',
        ]


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ['id', 'description']


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        contact_type = ContactTypeSerializer(many=True, read_only=True)
        ipa_code = ParticipantInstitutionSerializer()
        fields = [
                    'id',
                    'name',
                    'phone_number',
                    'email',
                    'priority',
                    'contact_type',
                    'ipa_code',
                ]

class GeneratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Generator
        site = SiteSerializer(many=True, read_only=True)
        fields = [
                    'id',
                    'power',
                    'manufacturer',
                    'patrimony',
                    'site',
                ]
