from rest_framework import viewsets
from .serializers import GBIC_TypeSerializer, GBICSerializer
from .models import GBIC, GBIC_Type


# Create your views here.
class GBICListViewSet(viewsets.ModelViewSet):
    queryset = GBIC.objects.all()
    serializer_class = GBICSerializer


class GBIC_TypeListViewSet(viewsets.ModelViewSet):
    queryset = GBIC_Type.objects.all()
    serializer_class = GBIC_TypeSerializer
