# from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
# from rest_framework.response import Response
from .serializers import SegmentSerializer
from .models import Segment


# Create your views here.
class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer
