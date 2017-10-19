from .models import InstitutionType, ParticipantInstitution
from .models import ContactType, Generator, AccessCable
from .models import NoBreak
from .models import Switch
from .models import Contact
from dgo.serializers import GODSerializer
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


class NoBreakSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoBreak
        fields = [
                'id',
                'power',
                'proprietary',
                'patrimony_number',
                'site_id',
        ]


class SwitchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Switch
        fields = [
                'serial_number',
                'fabricant',
                'slots_quantity',
                'patrimony_number',
                'site_id',
        ]


class AccessCableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessCable
        god_id = GODSerializer(many=True, read_only=True)
        site_id = SiteSerializer(many=True, read_only=True)
        fields = [
            'id',
            'length',
            'fiber_quantity',
            'cod',
            'site_id',
            'god_id',
        ]
