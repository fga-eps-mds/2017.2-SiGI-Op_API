from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Uplink
from .models import Segments
from .views import UplinkViewSet
from .views import SegmentsListViewSet
# Create your tests here.


class SegmentsTest(TestCase):

    def test_Segments_view_set(self):
        request = APIRequestFactory().get("")
        segments_detail = SegmentsListViewSet.as_view(actions={'get': 'retrieve'})
        Segmentstest = Segments.objects.create(
            number='404',
            length='25'
    )
        response = segments_detail(request, pk=Segmentstest.pk)
        self.assertEqual(response.status_code, 200)


class UplinkTest(TestCase):

    def test_Uplink_view_set(self):
        request = APIRequestFactory().get("")
        uplink_detail = UplinkListViewSet.as_view(actions={'get': 'retrieve'})
        Uplinktest = Uplink.objects.create(
            name_vlan = 'xablau'
            band = '66'
            code = '42'
    )
        response = uplink_detail(request, pk=Uplinktest.pk)
        self.assertEqual(response.status_code, 200)
