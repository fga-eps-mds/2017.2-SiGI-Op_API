from django.test import TestCase
from .models import CableStretch
from .views import CableStretchListViewSet
from rest_framework.test import APIRequestFactory


# Create your tests here.
class CableStretchTest(TestCase):
    def test_CableStretch_view_set(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       extinction_date="2017-10-12")
        response = cable_stretch_detail(request, pk=CableStretchtest.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_test_CableStretch_view_set(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       extinction_date="2017-10-12")
        primaryKey = CableStretchtest.pk
        CableStretchtest.delete()
        response = cable_stretch_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
