from ipa.models import Site, SiteType
from rest_framework import serializers



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
