from sigi_op.views import CustomViewSet
from .serializers import GBIC_TypeSerializer, GBICSerializer
from .models import GBIC, GBIC_Type


# Create your views here.
class GBICListViewSet(CustomViewSet):
    queryset = GBIC.objects.all().order_by('serial')
    serializer_class = GBICSerializer


class GBIC_TypeListViewSet(CustomViewSet):
    queryset = GBIC_Type.objects.all().order_by('description')
    serializer_class = GBIC_TypeSerializer
