from sigi_op.views import CustomViewSet
from .serializers import GBICTypeSerializer, GBICSerializer
from .models import GBIC, GBICType


# Create your views here.
class GBICListViewSet(CustomViewSet):
    class_name = GBIC
    order_param_name = 'serial'
    queryset = GBIC.objects.all().order_by('serial')
    serializer_class = GBICSerializer


class GBICTypeListViewSet(CustomViewSet):
    class_name = GBICType
    order_param_name = 'description'
    queryset = GBICType.objects.all().order_by('description')
    serializer_class = GBICTypeSerializer
