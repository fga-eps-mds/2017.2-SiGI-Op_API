from ipa.models import Site, SiteType
from rest_framework import serializers
from django.contrib.auth.models import User


class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteType
        fields = [
            'id',
            'description',
        ]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        site_type = SiteTypeSerializer(many=True, read_only=True)
        fields = [
            'id',
            'name',
            'lattitude',
            'longitude',
            'bandwidth',
            'ipa_code',
            'site_type',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
