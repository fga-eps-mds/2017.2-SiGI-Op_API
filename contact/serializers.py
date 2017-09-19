from rest_framework import serializers
from contact import models


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactType
        fields = ['id', 'name']


class ContactSerializer(serializers.ModelSerializer):
    contact_type = ContactTypeSerializer()

    class Meta:
        model = models.Contact
        fields = [
                    'id',
                    'name',
                    'phone_number',
                    'email',
                    'priority',
                    'contact_type']

    def create(self, validated_data):
        contact_type_data = validated_data.pop('contact_type')
        contact_type = models.ContactType.objects.create(**contact_type_data)
        contact = models.Contact.objects.create(contact_type=contact_type,
                                                **validated_data)
        return contact
