from django.test import TestCase
# Create your tests here.

from rest_framework.test import APIRequestFactory
from .models import EmendationBoxType
from .models import EmendationBoxStructure
from .views import EmendationBoxTypeListViewSet
from .views import EmendationBoxStructureListViewSet
from .models import Post
from dgo.models import GOD, GODPort, GODPortConnectionType
from .views import PostListViewSet

class EmendationBoxTest(TestCase):

    def test_emendationbox_type(self):
        request = APIRequestFactory().get("")
        view = EmendationBoxTypeListViewSet.as_view(actions={'get': 'retrieve'})
        emendationbox_type = EmendationBoxType.objects.create(
            description="RandomEmendationBox")

        response = view(request, pk=emendationbox_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_emendationbox_structure(self):
        request = APIRequestFactory().get("")
        view = EmendationBoxStructureListViewSet.as_view(actions={'get': 'retrieve'})
        emendationbox_structure = EmendationBoxStructure.objects.create(
            description="RandomEmendationBox")

        response = view(request, pk=emendationbox_structure.pk)
        self.assertEqual(response.status_code, 200)

    # def test_emendationbox(self):
    #    request = APIRequestFactory().get("")
    #    view = EmendationBoxListViewSet.as_view(actions={'get': 'retrieve'})
    #    emendationbox_type2 = EmendationBoxType.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox_structure2 = EmendationBoxStructure.objects.create(
    #        description="RandomEmendationBox2")
    #    emendationbox = EmendationBox.objects.create(
    #        lattitude=42,
    #        longitude=42,
    #        designNumber=13,
    #        access_box=True,
    #        creation_date=20170101,
    #        extinction_date=20180101,
    #        emendation_type = emendationbox_type2,
    #        emendation_structure = emendationbox_structure2)

    #    response = view(request, pk=emendationbox.pk)
    #    self.assertEqual(response.status_code, 200)

    # def test_emendationbox_delete(self):
    #    request = APIRequestFactory().get("")
    #    view = EmendationBoxListViewSet.as_view(actions={'get': 'retrieve'})
    #    emendationbox_type2 = EmendationBoxType.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox_structure2 = EmendationBoxStructure.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox = EmendationBox.objects.create(
    #        lattitude=42,
    #        longitude=42,
    #        designNumber=13,
    #        access_box=True,
    #        creation_date=20170101,
    #        extinction_date=20180101,
    #        emendation_type = emendationbox_type2,
    #        emendation_structure=emendationbox_type2)

    #    emendationbox.delete()
    #    response = view(request, pk=emendationbox.pk)
    #    self.assertEqual(response.status_code, 404)

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
