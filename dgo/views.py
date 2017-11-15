# from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
# from rest_framework.response import Response
from .serializers import GODSerializer, GODPortSerializer, JumperSerializer
from .serializers import GODPortConnectionTypeSerializer, AccessCableSerializer
from .models import GOD, GODPort, GODPortConnectionType, Jumper, AccessCable


# Create your views here.


class GODListViewSet(viewsets.ModelViewSet):
    queryset = GOD.objects.all()
    serializer_class = GODSerializer


class GODPortListViewSet(viewsets.ModelViewSet):
    queryset = GODPort.objects.all()
    serializer_class = GODPortSerializer


class GODPortConnectionTypeListViewSet(viewsets.ModelViewSet):
    queryset = GODPortConnectionType.objects.all()
    serializer_class = GODPortConnectionTypeSerializer


class JumperViewSet(viewsets.ModelViewSet):
    queryset = Jumper.objects.all()
    serializer_class = JumperSerializer


class AccessCableListViewSet(viewsets.ModelViewSet):
    queryset = AccessCable.objects.all()
    serializer_class = AccessCableSerializer
