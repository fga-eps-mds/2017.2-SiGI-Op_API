from sigi_op.views import CustomViewSet
from .serializers import EmendationBoxSerializer
from .serializers import EmendationBoxTypeSerializer
from .serializers import EmendationBoxStructureSerializer
from .models import EmendationBoxStructure, EmendationBoxType, EmendationBox


# Create your views here.
class EmendationBoxListViewSet(CustomViewSet):
    class_name = EmendationBox
    order_param_name = 'designNumber'
    queryset = EmendationBox.objects.all().order_by('designNumber')
    serializer_class = EmendationBoxSerializer


class EmendationBoxTypeListViewSet(CustomViewSet):
    class_name = EmendationBoxType
    order_param_name = 'description'
    queryset = EmendationBoxType.objects.all().order_by('description')
    serializer_class = EmendationBoxTypeSerializer


class EmendationBoxStructureListViewSet(CustomViewSet):
    class_name = EmendationBoxStructure
    order_param_name = 'description'
    queryset = EmendationBoxStructure.objects.all().order_by('description')
    serializer_class = EmendationBoxStructureSerializer
