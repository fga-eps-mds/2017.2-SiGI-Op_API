from rest_framework import viewsets
from .serializers import SegmentsSerializer
from .models import Segments


# Create your views here.
class SegmentsListViewSet(viewsets.ModelViewSet):
    queryset = Segments.objects.all()
    serializer_class = SegmentsSerializer
