from django.shortcuts import render
from rest_framework import viewsets
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer

# Create your views here.

class UplinkViewSet(viewsets.ModelViewSet):
    queryset = Uplink.objects.all()
    serializer_class = UplinkSerializer
