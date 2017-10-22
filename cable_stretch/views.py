# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CableStretchSerializer
from .serializers import CableStretchTypeSerializer
from .models import CableStretch
from .models import CableStretchType


# Create your views here.
class CableStretchListViewSet(viewsets.ModelViewSet):
    queryset = CableStretch.objects.all()
    serializer_class = CableStretchSerializer


class CableStretchTypeListViewSet(viewsets.ModelViewSet):
    queryset = CableStretchType.objects.all()
    serializer_class = CableStretchTypeSerializer
