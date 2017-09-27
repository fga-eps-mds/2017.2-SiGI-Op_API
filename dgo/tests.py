
from django.test import TestCase
from .models import GOD
from rest_framework.test import APIRequestFactory
from .views import GODListViewSet

class GODTest(TestCase):

    def test_GOD_view_set(self):
        request = APIRequestFactory().get("")
        GOD_detail = GODViewSet.as_view(actions={'get':'retrieve'})
        GOD = GOD.objects.create(code=1, fabricant='Potato Bread', port_quantity=4)
        response = GOD_detail(request, pk=GOD.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_GOD_view_set(self):
        request = APIRequestFactory().get("")
        GOD_detail = GODViewSet.as_view(actions={'get':'retrieve'})
        GOD = GOD.objects.create(code=666, fabricant='AC/DC', port_quantity='thirteen')
        primaryKey = GOD.pk
        GOD.delete()
        response = GOD_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
