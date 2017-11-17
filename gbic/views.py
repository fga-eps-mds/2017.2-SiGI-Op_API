from sigi_op.views import CustomViewSet
from .serializers import GBIC_TypeSerializer, GBICSerializer
from .models import GBIC, GBIC_Type


# Create your views here.
class GBICListViewSet(CustomViewSet):
    class_name = GBIC
    order_param_name = 'serial'
    queryset = GBIC.objects.all().order_by('serial')
    serializer_class = GBICSerializer


class GBIC_TypeListViewSet(CustomViewSet):
    class_name = GBIC_Type
    order_param_name = 'description'
    queryset = GBIC_Type.objects.all().order_by('description')
    serializer_class = GBIC_TypeSerializer
