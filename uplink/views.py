from sigi_op.views import CustomViewSet
from uplink.models import Uplink
from uplink.serializers import UplinkSerializer
from cable_stretch.models import CableStretch
from rest_framework.response import Response
from rest_framework import status
from .serializers import SegmentsSerializer
from .models import Segments


class UplinkViewSet(CustomViewSet):
    class_name = Uplink
    order_param_name = 'name_vlan'
    queryset = Uplink.objects.all().order_by('name_vlan')
    serializer_class = UplinkSerializer


class SegmentsListViewSet(CustomViewSet):
    class_name = Segments
    order_param_name = 'number'
    queryset = Segments.objects.all().order_by('number')
    serializer_class = SegmentsSerializer

    def create(self, request):  # pylint: disable=arguments-differ
        segment_data = {
            'number': request.data['number'],
            'length': request.data['length'],
            'dgos': request.data['dgos'],
            'emendation_boxes': request.data['emendation_boxes']
        }
        serializer = SegmentsSerializer(data=segment_data)

        response = 0

        if serializer.is_valid():
            cable_stretch_quantity = request.data['cable_stretch_quantity']
            number = request.data['number']
            stretch_list = []
            for i in range(cable_stretch_quantity):
                stretch_list.append(CableStretch(cod=str(number)+"_"+str(i)))
            CableStretch.objects.bulk_create(stretch_list)
            # Saves a list of cable stretch
            serializer.save()
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        return response
