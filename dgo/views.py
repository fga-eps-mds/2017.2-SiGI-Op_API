# from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
# from rest_framework.response import Response
from .serializers import GODSerializer, GODPortSerializer
from .serializers import GODPortConnectionTypeSerializer
from .models import GOD, GODPort, GODPortConnectionType


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
