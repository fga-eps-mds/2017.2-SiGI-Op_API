from sigi_op.views import CustomViewSet
from .serializers import EmendationBoxSerializer
from .serializers import EmendationBoxTypeSerializer
from .serializers import EmendationBoxStructureSerializer
from .models import EmendationBoxStructure, EmendationBoxType, EmendationBox


# Create your views here.
class EmendationBoxListViewSet(CustomViewSet):
    queryset = EmendationBox.objects.all().order_by('designNumber')
    serializer_class = EmendationBoxSerializer


class EmendationBoxTypeListViewSet(CustomViewSet):
    queryset = EmendationBoxType.objects.all().order_by('description')
    serializer_class = EmendationBoxTypeSerializer


class EmendationBoxStructureListViewSet(CustomViewSet):
    queryset = EmendationBoxStructure.objects.all().order_by('description')
    serializer_class = EmendationBoxStructureSerializer
