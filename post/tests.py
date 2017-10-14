from django.test import TestCase
from .models import Post
from dgo.models import GOD, GODPort, GODPortConnectionType
from emendation_box.models import EmendationBox
from emendation_box.models import EmendationBoxType
from emendation_box.models import EmendationBoxStructure
from rest_framework.test import APIRequestFactory
from .views import PostListViewSet

class PostTest(TestCase):

    def test_Post_view_set(self):
        request = APIRequestFactory().get("")
        Post_detail = PostListViewSet.as_view(actions={'get':'retrieve'})
        GODt = GOD.objects.create(code=1, fabricant='Potato Bread', port_quantity=4)
        emendationbox = EmendationBox.objects.create(
               lattitude=42,
               longitude=42,
               designNumber=13,
               access_box=True,
               creation_date="2017-10-06",
               extinction_date="2017-10-06",
               emendation_type = EmendationBoxType.objects.create(
                       description=1),
               emendation_structure = EmendationBoxStructure.objects.create(
                       description=2))
        Posttest = Post.objects.create(cable_length=1, stretch=1, emendation_box=emendationbox , god=GODt)
        response = Post_detail(request, pk=Posttest.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_Post_view_set(self):
        request = APIRequestFactory().get("")
        Post_detail = PostListViewSet.as_view(actions={'get':'retrieve'})
        GODt = GOD.objects.create(code=1, fabricant='Potato Bread', port_quantity=4)
        emendationbox = EmendationBox.objects.create(
               lattitude=42,
               longitude=42,
               designNumber=13,
               access_box=True,
               creation_date="2017-10-06",
               extinction_date="2017-10-06",
               emendation_type = EmendationBoxType.objects.create(
                       description=1),
               emendation_structure = EmendationBoxStructure.objects.create(
                       description=2))
        Posttest = Post.objects.create(cable_length=1, stretch=1, emendation_box=emendationbox , god=GODt)
        primaryKey = Posttest.pk
        Posttest.delete()
        response = Post_detail(request,pk=primaryKey)
        self.assertEqual(response.status_code,404)
