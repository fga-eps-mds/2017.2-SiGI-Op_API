# from django.shortcuts import render
from sigi_op.views import CustomViewSet
from .serializers import CableStretchSerializer
from .serializers import CableStretchTypeSerializer
from .serializers import TubelooseSerializer
from .models import CableStretch, CableStretchType
from .models import Tubeloose


# Create your views here.
class CableStretchTypeListViewSet(CustomViewSet):
    class_name = CableStretchType
    order_param_name = 'description'
    queryset = CableStretchType.objects.all().order_by('description')
    serializer_class = CableStretchTypeSerializer


class CableStretchListViewSet(CustomViewSet):
    class_name = CableStretch
    order_param_name = 'fabricant'
    queryset = CableStretch.objects.all().order_by('fabricant')
    serializer_class = CableStretchSerializer


class TubelooseListViewSet(CustomViewSet):
    class_name = Tubeloose
    order_param_name = 'stretch_id'
    queryset = Tubeloose.objects.all().order_by('stretch_id')
    serializer_class = TubelooseSerializer
