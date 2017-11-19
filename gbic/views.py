from sigi_op.views import CustomViewSet
from .serializers import GBICTypeSerializer, GBICSerializer
from .models import GBIC, GBICType


# Create your views here.
class GBICListViewSet(CustomViewSet):
    queryset = GBIC.objects.all().order_by('serial')
    serializer_class = GBICSerializer


class GBICTypeListViewSet(CustomViewSet):
    queryset = GBICType.objects.all().order_by('description')
    serializer_class = GBICTypeSerializer
