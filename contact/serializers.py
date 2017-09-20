from rest_framework import serializers
from contact import models


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactType
        fields = ['id', 'name']

    def __str__(self, value):
        return '%s' % (self.name)


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contact
        contact_type = ContactTypeSerializer(many=True, read_only=True)
        fields = [
                    'id',
                    'name',
                    'phone_number',
                    'email',
                    'priority',
                    'contact_type']
