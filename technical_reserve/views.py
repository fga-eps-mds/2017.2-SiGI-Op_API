# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .serializers import TechnicalReserveSerializer
from .models import TechnicalReserve


class TechnicalReserveListViewSet(viewsets.ModelViewSet):
    queryset = TechnicalReserve.objects.all()
    serializer_class = TechnicalReserveSerializer
