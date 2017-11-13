# from django.shortcuts import get_object_or_404, render
from sigi_op.views import CustomViewSet
# from rest_framework.response import Response
from .serializers import GODSerializer, GODPortSerializer, JumperSerializer
from .serializers import GODPortConnectionTypeSerializer, AccessCableSerializer
from .models import GOD, GODPort, GODPortConnectionType, Jumper, AccessCable


# Create your views here.


class GODListViewSet(CustomViewSet):
    queryset = GOD.objects.all().order_by('site_id')
    serializer_class = GODSerializer


class GODPortListViewSet(CustomViewSet):
    queryset = GODPort.objects.all().order_by('god_id')
    serializer_class = GODPortSerializer


class GODPortConnectionTypeListViewSet(CustomViewSet):
    queryset = GODPortConnectionType.objects.all().order_by('code')
    serializer_class = GODPortConnectionTypeSerializer


class JumperViewSet(CustomViewSet):
    queryset = Jumper.objects.all().order_by('god_port1')
    serializer_class = JumperSerializer


class AccessCableListViewSet(CustomViewSet):
    queryset = AccessCable.objects.all().order_by('site_id')
    serializer_class = AccessCableSerializer
