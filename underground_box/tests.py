from django.test import TestCase
from rest_framework.test import APIRequestFactory
from emendation_box.models import EmendationBox
from emendation_box.models import EmendationBoxType
from emendation_box.models import EmendationBoxStructure
from technical_reserve.models import TechnicalReserve
from .models import UndergroundBox
from .models import UndergroundBoxType
from .views import UndergroundBoxTypeViewSet
from .views import UndergroundBoxViewSet

class UndergroundBoxTest(TestCase):
    def test_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        response = undergroundbox_type_detail(request, pk=undergroundbox_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_undergroundbox_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        emendationtype = EmendationBoxType.objects.create(description="IHATEIT")
        structure = EmendationBoxStructure.objects.create(description="SERIOUSLY")
        emendationbox = EmendationBox.objects.create(
            lattitude=42.42,
            longitude=42.42,
            designNumber=42,
            access_box=True,
            creation_date="2017-01-01",
            extinction_date="2018-01-01",
            emendation_type=emendationtype,
            emendation_structure=structure,
        )
        reserve = TechnicalReserve.objects.create(
            code=666,
            length=8008.5,
            lattitude=8001,
            longitude=9001
        )
        undergroundbox = UndergroundBox.objects.create(
            box_type=undergroundbox_type,
            code=123,
            lattitude=123,
            cover_type="Cover type",
            longitude=321,
            emendation_box=emendationbox,
            technical_reserve=reserve
        )
        response = undergroundbox_detail(request, pk=undergroundbox.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Fundergroundbox")
        primary_key = undergroundbox_type.pk
        undergroundbox_type.delete()
        response = undergroundbox_type_detail(request, pk=primary_key)
        self.assertEqual(response.status_code, 404)

    def test_wrong_view_set(self):
        request = APIRequestFactory().get("")

        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        emendationtype = EmendationBoxType.objects.create(description="IHATEIT")
        structure = EmendationBoxStructure.objects.create(description="TOOMUCH")
        emendationbox = EmendationBox.objects.create(
            lattitude=42.42,
            longitude=42.42,
            designNumber=42,
            emendation_type=emendationtype,
            access_box=True,
            emendation_structure=structure,
            creation_date="2017-01-01",
            extinction_date="2018-01-01",
        )
        reserve = TechnicalReserve.objects.create(
            code=666,
            length=8008.5,
            lattitude=8001,
            longitude=9001
        )
        undergroundbox = UndergroundBox.objects.create(
            box_type=undergroundbox_type,
            code=123,
            lattitude=123,
            cover_type="Cover type",
            longitude=321,
            emendation_box=emendationbox,
            technical_reserve=reserve
        )
        primary_key = undergroundbox.pk
        undergroundbox.delete()
        response = undergroundbox_detail(request, pk=primary_key)
        self.assertEqual(response.status_code, 404)
