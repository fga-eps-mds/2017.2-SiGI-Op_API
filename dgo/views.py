from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from sigi_op.serializers import GODSerializer
from .models import GOD

# Create your views here.
class GODListViewSet(viewsets.ModelViewSet):
    queryset = GOD.objects.all()
    serializer_class = GODSerializer
