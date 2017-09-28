from .serializers import Segments_serializer_class
from rest_framework import viewsets
from .models import Segment


class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = Segments_serializer_class
