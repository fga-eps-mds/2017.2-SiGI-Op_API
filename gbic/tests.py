from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import GBIC, GBICType
from .views import GBICListViewSet


# Create your tests here.
class GBICTest(TestCase):

    def test_gbic_view_set(self):
        request = APIRequestFactory().get("")
        gbic_detail = GBICListViewSet.as_view(actions={'get': 'retrieve'})
        gbic_type_test = GBICType.objects.create(description='muito_bom')
        gbic_test = GBIC.objects.create(
            serial='showdaxuxa',
            patrimony_number='666',
            gbic_type=gbic_type_test
        )
        response = gbic_detail(request, pk=gbic_test.pk)
        self.assertEqual(response.status_code, 200)


    def test_deleted_gbic_view_set(self):
        request = APIRequestFactory().get("")
        gbic_detail = GBICListViewSet.as_view(actions={'get': 'retrieve'})
        gbic_type_test = GBICType.objects.create(description='muitoruim')
        gbic_test = GBIC.objects.create(
            serial='showdomilhao',
            patrimony_number='777',
            gbic_type=gbic_type_test
        )
        gbic_test.delete()
        response = gbic_detail(request, pk=gbic_test.pk)
        self.assertEqual(response.status_code, 404)
