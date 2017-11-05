# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CableStretchSerializer
from .serializers import CableStretchTypeSerializer
from .serializers import TubelooseSerializer
from .models import CableStretch, CableStretchType
from .models import Tubeloose


# Create your views here.
class CableStretchTypeListViewSet(viewsets.ModelViewSet):
    queryset = CableStretchType.objects.all().order_by('description')
    serializer_class = CableStretchTypeSerializer


class CableStretchListViewSet(viewsets.ModelViewSet):
    queryset = CableStretch.objects.all().order_by('fabricant')
    serializer_class = CableStretchSerializer


class TubelooseListViewSet(viewsets.ModelViewSet):
    queryset = Tubeloose.objects.all().order_by('stretch_id')
    serializer_class = TubelooseSerializer
