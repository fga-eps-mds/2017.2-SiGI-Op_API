# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CableStretchSerializer
from .serializers import TubelooseSerializer
from .models import CableStretch
from .models import Tubeloose


# Create your views here.
class CableStretchListViewSet(viewsets.ModelViewSet):
    queryset = CableStretch.objects.all()
    serializer_class = CableStretchSerializer


class TubelooseListViewSet(viewsets.ModelViewSet):
    queryset = Tubeloose.objects.all()
    serializer_class = TubelooseSerializer
