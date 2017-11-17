from sigi_op.views import CustomViewSet
from underground_box.models import UndergroundBox, UndergroundBoxType
from underground_box.serializers import UndergroundBoxSerializer
from underground_box.serializers import UndergroundBoxTypeSerializer


class UndergroundBoxTypeViewSet(CustomViewSet):
    class_name = UndergroundBoxType
    order_param_name = 'name'
    queryset = UndergroundBoxType.objects.all().order_by('name')
    serializer_class = UndergroundBoxTypeSerializer


class UndergroundBoxViewSet(CustomViewSet):
    class_name = UndergroundBox
    order_param_name = 'emendation_box'
    queryset = UndergroundBox.objects.all().order_by('emendation_box')
    serializer_class = UndergroundBoxSerializer
