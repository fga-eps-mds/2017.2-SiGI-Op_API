from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import CableStretch, CableStretchType
from .models import Tubeloose
from .views import CableStretchListViewSet
from .views import TubelooseListViewSet


# Create your tests here.
class CableStretchTest(TestCase):
    def test_cable_stretch_view_set(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        cabletype = CableStretchType.objects.create(description="random")
        cable_stretch_test = CableStretch.objects.create(cod=1,
                                                         length=1,
                                                         manufacturing_year=2012,
                                                         infrastructure="random",
                                                         owner="random",
                                                         fabricant='Potato Bread',
                                                         cable_stretch_type=cabletype,
                                                         access=False,
                                                         creation_date="2017-10-12",
                                                         updated_date="2017-10-12")
        response = cable_stretch_detail(request, pk=cable_stretch_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_cable_stretch(self):
        request = APIRequestFactory().get("")
        cable_stretch_detail = CableStretchListViewSet.as_view(actions={'get':'retrieve'})
        cabletype = CableStretchType.objects.create(description="random")
        cable_stretch_test = CableStretch.objects.create(cod=1,
                                                         length=1,
                                                         manufacturing_year=2012,
                                                         infrastructure="random",
                                                         owner="random",
                                                         fabricant='Potato Bread',
                                                         cable_stretch_type=cabletype,
                                                         access=False,
                                                         creation_date="2017-10-12",
                                                         updated_date="2017-10-12")
        primary_key = cable_stretch_test.pk
        cable_stretch_test.delete()
        response = cable_stretch_detail(request, pk=primary_key)
        self.assertEqual(response.status_code, 404)

    def test_tubeloose_view_set(self):
        request = APIRequestFactory().get("")
        cabletype = CableStretchType.objects.create(description="random")
        cable_stretch_test = CableStretch.objects.create(length=1,
                                                         manufacturing_year=2012,
                                                         cod=1,
                                                         infrastructure="random",
                                                         owner="random",
                                                         fabricant='Potato Bread',
                                                         cable_stretch_type=cabletype,
                                                         access=False,
                                                         creation_date="2017-10-12",
                                                         updated_date="2017-10-12")
        tubeloose_detail = TubelooseListViewSet.as_view(actions={'get':'retrieve'})
        tubeloose_test = Tubeloose.objects.create(number=1010,
                                                  stretch_id=cable_stretch_test)
        response = tubeloose_detail(request, pk=tubeloose_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_tubeloose_view_set(self):
        request = APIRequestFactory().get("")
        cabletype = CableStretchType.objects.create(description="random")
        cable_stretch_test = CableStretch.objects.create(length=1,
                                                         manufacturing_year=2012,
                                                         cod=1,
                                                         infrastructure="random",
                                                         owner="random",
                                                         fabricant='Potato Bread',
                                                         cable_stretch_type=cabletype,
                                                         access=False,
                                                         creation_date="2017-10-12",
                                                         updated_date="2017-10-12")
        tubeloose_detail = TubelooseListViewSet.as_view(actions={'get':'retrieve'})
        tubeloose_test = Tubeloose.objects.create(number=1010,
                                                  stretch_id=cable_stretch_test)
        primary_key = tubeloose_test.pk
        tubeloose_test.delete()
        response = tubeloose_detail(request, pk=primary_key)
        self.assertEqual(response.status_code, 404)
