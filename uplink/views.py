from rest_framework import viewsets
from .serializers import UplinkSerializer
from .models import Uplink

# Create your views here
class UplinkViewSet(viewsets.ModelViewSet):
    queryset = Uplink.objects.all()
    serializer_class = UplinkSerializer
