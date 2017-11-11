from django.test import TestCase
from .models import UndergroundBox
from rest_framework.test import APIRequestFactory

from .models import UndergroundBoxType
from emendation_box.models import EmendationBox
from emendation_box.models import EmendationBoxType
from emendation_box.models import EmendationBoxStructure
from technical_reserve.models import TechnicalReserve

from .views import UndergroundBoxTypeViewSet
from .views import UndergroundBoxViewSet

class UndergroundBoxTest(TestCase):
    def test_undergroundbox_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox") 
        response = undergroundbox_type_detail(request, pk=undergroundbox_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_undergroundbox_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Fundergroundbox") 
        primaryKey = undergroundbox_type.pk
        undergroundbox_type.delete()
        response = undergroundbox_type_detail(request, pk=primaryKey)
        self.assertEqual(response.status_code, 404)

    def test_undergroundbox_view_set(self):
        request = APIRequestFactory().get("")

        emendation_box_type = EmendationBoxType.objects.create(description="description")
        emendation_box_structure = EmendationBoxStructure.objects.create(description="description")
        emendation_box = EmendationBox.objects.create(lattitude=123,longitude=132,designNumber=123,
            access_box=True,creation_date="2017-10-18",extinction_date="2017-10-18",
            emendation_type=emendation_box_type,emendation_structure=emendation_box_structure)

        technical_reserve = TechnicalReserve.objects.create(code=1212,length=12,
            latitude=13,longitude=13)

        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        undergroundbox = UndergroundBox.objects.create(code="123code",box_type=undergroundbox_type, 
                latitude=123,longitude=321,cover_type="Cover type",emendation_box=emendation_box,
                technical_reserve=technical_reserve)
        response = undergroundbox_detail(request, pk=undergroundbox.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_undergroundbox_view_set(self):
        request = APIRequestFactory().get("")
        emendation_box_type = EmendationBoxType.objects.create(description="description")
        emendation_box_structure = EmendationBoxStructure.objects.create(description="description")
        emendation_box = EmendationBox.objects.create(lattitude=123,longitude=132,designNumber=123,
            access_box=True,creation_date="2017-10-18",extinction_date="2017-10-18",
            emendation_type=emendation_box_type,emendation_structure=emendation_box_structure)

        technical_reserve = TechnicalReserve.objects.create(code=1212,length=12,
            latitude=13,longitude=13)

        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        undergroundbox = UndergroundBox.objects.create(code="123code",box_type=undergroundbox_type, 
                latitude=123,longitude=321,cover_type="Cover type",emendation_box=emendation_box,
                technical_reserve=technical_reserve)
        primaryKey = undergroundbox.pk
        undergroundbox.delete()
        response = undergroundbox_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
