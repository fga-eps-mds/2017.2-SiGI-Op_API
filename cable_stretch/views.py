# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CableStretchSerializer
from .models import CableStretch


# Create your views here.
class CableStretchListViewSet(viewsets.ModelViewSet):
    queryset = CableStretch.objects.all()
    serializer_class = CableStretchSerializer
