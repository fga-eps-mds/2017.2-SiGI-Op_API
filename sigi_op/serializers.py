from ipa.models import Site, SiteType
from rest_framework import serializers



class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteType
        fields = [
            'type_id',
            'name',
        ]

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        site_type = SiteTypeSerializer(many=True, read_only=True)
        fields = [
            'site_id',
            'name',
            'lattitude',
            'longitude',
            'bandwidth',
            'IPa_code',
            'type_site',
        ]
