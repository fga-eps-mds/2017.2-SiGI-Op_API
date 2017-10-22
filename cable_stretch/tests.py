from django.test import TestCase
from .models import CableStretch, CableStretchType
from .models import Tubeloose
from .views import CableStretchListViewSet
from .views import TubelooseListViewSet
from rest_framework.test import APIRequestFactory


# Create your tests here.
class CableStretchTest(TestCase):
    def test_CableStretch_view_set(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        cabletype = CableStretchType.objects.create(description="random")
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       cable_stretch_type = cabletype,
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       updated_date="2017-10-12")
        response = cable_stretch_detail(request, pk=CableStretchtest.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_test_CableStretch_view_set(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        cabletype = CableStretchType.objects.create(description="random")
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       cable_stretch_type = cabletype,
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       updated_date="2017-10-12")
        primaryKey = CableStretchtest.pk
        CableStretchtest.delete()
        response = cable_stretch_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)

    def test_Tubeloose_view_set(self):
        request = APIRequestFactory().get("")
        cabletype = CableStretchType.objects.create(description="random")
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       cable_stretch_type = cabletype,
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       updated_date="2017-10-12")
        tubeloose_detail = TubelooseListViewSet.as_view(actions={'get':'retrieve'})
        Tubeloosetest = Tubeloose.objects.create(number=1010,
                                                 stretch_id=CableStretchtest)
        response = tubeloose_detail(request, pk=Tubeloosetest.pk)
        self.assertEqual(response.status_code,200)

    def test_wrong_Tubeloose_view_set(self):
        request = APIRequestFactory().get("")
        cabletype = CableStretchType.objects.create(description="random")
        CableStretchtest = CableStretch.objects.create(length=1,
                                                       manufacturing_year=2012,
                                                       infrastructure="random",
                                                       owner="random",
                                                       fabricant='Potato Bread',
                                                       cable_stretch_type = cabletype,
                                                       access=False,
                                                       creation_date="2017-10-12",
                                                       updated_date="2017-10-12")
        tubeloose_detail = TubelooseListViewSet.as_view(actions={'get':'retrieve'})
        Tubeloosetest = Tubeloose.objects.create(number=1010,
                                                 stretch_id=CableStretchtest)
        primaryKey = Tubeloosetest.pk
        Tubeloosetest.delete()
        response = tubeloose_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
