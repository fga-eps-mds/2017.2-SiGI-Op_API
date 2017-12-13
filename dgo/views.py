# from django.shortcuts import get_object_or_404, render
from sigi_op.views import CustomViewSet
# from rest_framework.response import Response
from .serializers import GODSerializer, GODPortSerializer, JumperSerializer
from .serializers import GODPortConnectionTypeSerializer, AccessCableSerializer
from .serializers import GODFabricantSerializer, GODFabricantModelSerializer
from .models import GOD, GODPort, GODPortConnectionType, Jumper, AccessCable
from .models import GODFabricant, GODFabricantModel


# Create your views here.

class GODFabricantListViewSet(CustomViewSet):
    class_name = GODFabricant
    order_param_name = 'pk'
    queryset = GODFabricant.objects.all().order_by('pk')
    serializer_class = GODFabricantSerializer


class GODFabricantModelListViewSet(CustomViewSet):
    class_name = GODFabricantModel
    order_param_name = 'pk'
    queryset = GODFabricantModel.objects.all().order_by('pk')
    serializer_class = GODFabricantModelSerializer


class GODListViewSet(CustomViewSet):
    class_name = GOD
    order_param_name = 'site_id'
    queryset = GOD.objects.all().order_by('site_id')
    serializer_class = GODSerializer


class GODPortListViewSet(CustomViewSet):
    class_name = GODPort
    order_param_name = 'god_id'
    queryset = GODPort.objects.all().order_by('god_id')
    serializer_class = GODPortSerializer


class GODPortConnectionTypeListViewSet(CustomViewSet):
    class_name = GODPortConnectionType
    order_param_name = 'code'
    queryset = GODPortConnectionType.objects.all().order_by('code')
    serializer_class = GODPortConnectionTypeSerializer


class JumperViewSet(CustomViewSet):
    class_name = Jumper
    order_param_name = 'god_port1'
    queryset = Jumper.objects.all().order_by('god_port1')
    serializer_class = JumperSerializer


class AccessCableListViewSet(CustomViewSet):
    class_name = AccessCable
    order_param_name = 'site_id'
    queryset = AccessCable.objects.all().order_by('site_id')
    serializer_class = AccessCableSerializer
