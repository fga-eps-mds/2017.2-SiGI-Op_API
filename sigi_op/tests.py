import emendation_box.models
import ipa.models
import underground_box.models
from technical_reserve.models import TechnicalReserve
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import networkmap

class MapTest(TestCase):
    def set_up(self):
        emendationbox_type = emendation_box.models.EmendationBoxType.objects.create(
            description="RandomType")
        emendationbox_structure = emendation_box.models.EmendationBoxStructure.objects.create(
            description="RandomStructure")
        emendationbox = emendation_box.models.EmendationBox.objects.create(
            lattitude=42,
            longitude=42,
            designNumber=13,
            access_box=True,
            creation_date=20170101,
            extinction_date=20180101,
            emendation_type=emendationbox_type,
            emendation_structure=emendationbox_structure)

        instituion_type = ipa.models.InstitutionType.objects.create(
            description="RandomInstitution")
        instituition = ipa.models.ParticipantInstitution.objects.create(
            name='UnB', institution_type=instituion_type)
        site_type = ipa.models.SiteType.objects.create(
            description="RandomSiteType")
        ipa.models.Site.objects.create(
            name='RandomSite',
            lattitude=42,
            longitude=42,
            bandwidth=42,
            ipa_code=instituition,
            site_type=site_type)
        technical_reserve = TechnicalReserve.objects.create(
            code=1,
            length=1,
            lattitude=42,
            longitude=42)

        undergroundbox_type = underground_box.models.UndergroundBoxType.objects.create(
            name="Random undergroundBox")
        underground_box.models.UndergroundBox.objects.create(
            box_type=undergroundbox_type,
            code=1,
            lattitude=42,
            cover_type="Cover type",
            longitude=42,
            emendation_box=emendationbox,
            technical_reserve=technical_reserve
        )

        def test_map_view(self): #pylint: disable=unused-variable
            request = APIRequestFactory().get("")
            self.setUp()
            view = networkmap.as_view(actions={'get': 'retrieve'})
            response = view(request)
            self.assertEqual(response.status_code, 200)
