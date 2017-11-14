from sigi_op.views import CustomViewSet
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer
from .serializers import SegmentsSerializer
from .models import Segments


class UplinkViewSet(CustomViewSet):
    queryset = Uplink.objects.all().order_by('name_vlan')
    serializer_class = UplinkSerializer


class SegmentsListViewSet(CustomViewSet):
    queryset = Segments.objects.all()
    serializer_class = SegmentsSerializer
