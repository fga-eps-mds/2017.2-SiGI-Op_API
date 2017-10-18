#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccessCableSerializer
from .models import AccessCable

# Create your views here.

class AccessCableListViewSet(viewsets.ModelViewSet):
    queryset = AccessCable.objects.all()
    serializer_class = AccessCableSerializer
