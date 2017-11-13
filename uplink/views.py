from sigi_op.views import CustomViewSet
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer

# Create your views here.


class UplinkViewSet(CustomViewSet):
    queryset = Uplink.objects.all().order_by('name_vlan')
    serializer_class = UplinkSerializer
