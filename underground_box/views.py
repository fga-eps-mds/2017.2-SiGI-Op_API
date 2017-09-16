from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from underground_box.models import UndergroundBox
from underground_box.serializers import UndergroundBoxSerializer

class UndergroundBoxViewSet(viewsets.ModelViewSet):
    queryset = UndergroundBox.objects.all()
    serializer_class = UndergroundBoxSerializer

