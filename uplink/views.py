from rest_framework import viewsets
from .serializers import UplinkSerializer
from .serializers import SegmentsSerializer
from .models import Uplink
from .models import Segments


# Create your views here
class UplinkViewSet(viewsets.ModelViewSet):
    queryset = Uplink.objects.all()
    serializer_class = UplinkSerializer


class SegmentsListViewSet(viewsets.ModelViewSet):
    queryset = Segments.objects.all()
    serializer_class = SegmentsSerializer
