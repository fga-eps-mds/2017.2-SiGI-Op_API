from rest_framework import viewsets
from .serializers import UplinkSerializer
from .serializers import SegmentsSerializer
from .models import Uplink
from .models import Segments
from cable_stretch.models import CableStretch
from rest_framework.response import Response
from rest_framework import status


class UplinkViewSet(viewsets.ModelViewSet):
    queryset = Uplink.objects.all()
    serializer_class = UplinkSerializer


class SegmentsListViewSet(viewsets.ModelViewSet):
    queryset = Segments.objects.all()
    serializer_class = SegmentsSerializer

    def create(self, request):
        segment_data = {
            'number': request.data['number'],
            'length': request.data['length']
        }
        serializer = SegmentsSerializer(data=segment_data)
        if(serializer.is_valid()):
            cable_stretch_quantity = request.data['cable_stretch_quantity']
            number = request.data['number']
            stretch_list = []
            for i in range(cable_stretch_quantity):
                stretch_list.append(CableStretch(cod=str(number)+"_"+str(i)))
            CableStretch.objects.bulk_create(stretch_list)
            # Saves a list of cable stretch
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
