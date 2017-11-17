from sigi_op.views import CustomViewSet
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer
from .serializers import SegmentsSerializer
from .models import Segments


class UplinkViewSet(CustomViewSet):
    class_name = Uplink
    order_param_name = 'name_vlan'
    queryset = Uplink.objects.all().order_by('name_vlan')
    serializer_class = UplinkSerializer


class SegmentsListViewSet(CustomViewSet):
    class_name = Segments
    order_param_name = 'number'
    queryset = Segments.objects.all().order_by('number')
    serializer_class = SegmentsSerializer
