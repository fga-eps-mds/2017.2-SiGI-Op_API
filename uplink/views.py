from rest_framework import viewsets
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer

# Create your views here.


class UplinkViewSet(viewsets.ModelViewSet):
    queryset = Uplink.objects.all().order_by('name_vlan')
    serializer_class = UplinkSerializer
