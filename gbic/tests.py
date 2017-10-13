from django.test import TestCase
from .models import GBIC, GBIC_Type
from rest_framework.test import APIRequestFactory
from .views import GBIC_TypeListViewSet, GBICListViewSet


# Create your tests here.
class GBICTest(TestCase):

    def test_GBIC_view_set(self):
        request = APIRequestFactory().get("")
        GBIC_detail = GBICListViewSet.as_view(actions={'get': 'retrieve'})
        GbicTypeTest = GBIC_Type.objects.create(description='muito_bom')
        GBICtest = GBIC.objects.create(
            serial='showdaxuxa',
            patrimony_number='666',
            gbic_type = GbicTypeTest
        )
        response = GBIC_detail(request, pk=GBICtest.pk)
        self.assertEqual(response.status_code, 200)


    def test_deleted_GBIC_view_set(self):
        request = APIRequestFactory().get("")
        GBIC_detail = GBICListViewSet.as_view(actions={'get': 'retrieve'})
        GbicTypeTest = GBIC_Type.objects.create(description='muitoruim')
        GBICtest = GBIC.objects.create(
            serial='showdomilhao',
            patrimony_number='777',
            gbic_type = GbicTypeTest
        )
        GBICtest.delete()
        response = GBIC_detail(request, pk=GBICtest.pk)
        self.assertEqual(response.status_code, 404)
