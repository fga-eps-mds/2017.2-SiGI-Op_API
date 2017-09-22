# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import TechnicalReserveSerializer
from .models import TechnicalReserve


class TechnicalReserveListViewSet(viewsets.ModelViewSet):
    queryset = TechnicalReserve.objects.all()
    serializer_class = TechnicalReserveSerializer
