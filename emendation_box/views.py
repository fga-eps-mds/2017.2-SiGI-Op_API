from rest_framework import viewsets
from .serializers import EmendationBoxSerializer
from .serializers import EmendationBoxTypeSerializer
from .serializers import EmendationBoxStructureSerializer
from .models import EmendationBoxStructure, EmendationBoxType, EmendationBox


# Create your views here.
class EmendationBoxListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBox.objects.all()
    serializer_class = EmendationBoxSerializer


class EmendationBoxTypeListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBoxType.objects.all()
    serializer_class = EmendationBoxTypeSerializer


class EmendationBoxStructureListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBoxStructure.objects.all()
    serializer_class = EmendationBoxStructureSerializer
