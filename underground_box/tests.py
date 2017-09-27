from django.test import TestCase
from .models import UndergroundBox
from rest_framework.test import APIRequestFactory
from .models import UndergroundBoxType
from .views import UndergroundBoxTypeViewSet
from .views import UndergroundBoxViewSet

class UndergroundBoxTest(TestCase):
    def test_undergroundbox_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox") 
        response = undergroundbox_type_detail(request, pk=undergroundbox_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_undergroundbox_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Random undergroundBox")
        undergroundbox = UndergroundBox.objects.create(box_type=undergroundbox_type, 
                latitude=123,cover_type="Cover type",longitude=321,draw_number=10101)
        response = undergroundbox_detail(request, pk=undergroundbox.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_undergroundbox_type_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_type_detail = UndergroundBoxTypeViewSet.as_view(actions={'get': 'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="Fundergroundbox") 
        primaryKey = undergroundbox_type.pk
        undergroundbox_type.delete()
        response = undergroundbox_type_detail(request, pk=primaryKey)
        self.assertEqual(response.status_code, 404)

    def test_wrong_undergroundbox_view_set(self):
        request = APIRequestFactory().get("")
        undergroundbox_detail = UndergroundBoxViewSet.as_view(actions={'get':'retrieve'})
        undergroundbox_type = UndergroundBoxType.objects.create(name="PickleRick")
        undergroundbox = UndergroundBox.objects.create(box_type=undergroundbox_type,
                latitude=123,cover_type="Cover type",longitude=321,draw_number=10101)
        primaryKey = undergroundbox.pk
        undergroundbox.delete()
        response = undergroundbox_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
