from rest_framework import viewsets
from underground_box.models import UndergroundBox, UndergroundBoxType
from underground_box.serializers import UndergroundBoxSerializer
from underground_box.serializers import UndergroundBoxTypeSerializer


class UndergroundBoxTypeViewSet(viewsets.ModelViewSet):
    queryset = UndergroundBoxType.objects.all()
    serializer_class = UndergroundBoxTypeSerializer


class UndergroundBoxViewSet(viewsets.ModelViewSet):
    queryset = UndergroundBox.objects.all()
    serializer_class = UndergroundBoxSerializer
