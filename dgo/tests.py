from django.test import TestCase
from rest_framework.test import APIRequestFactory
from gbic.models import GBIC, GBIC_Type
from ipa.models import Site, SiteType, ParticipantInstitution, InstitutionType
from .views import GODListViewSet, GODPortConnectionTypeListViewSet, GODPortListViewSet
from .views import JumperViewSet, AccessCableListViewSet
from .models import GOD, GODPort, GODPortConnectionType, Jumper, AccessCable

class GODTest(TestCase):

    def test_god_view_set(self):
        request = APIRequestFactory().get("")
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)

        sitetype = SiteType.objects.create(description='IDK What Am I Doing')
        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        god_detail = GODListViewSet.as_view(actions={'get':'retrieve'})
        god_test = GOD.objects.create(code=1,
                                      fabricant='Potato Bread',
                                      port_quantity=4,
                                      site_id=sitetest)

        response = god_detail(request, pk=god_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_god_view_set(self):
        request = APIRequestFactory().get("")
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)
        sitetype = SiteType.objects.create(description='IDK What Am I Doing')
        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        god_detail = GODListViewSet.as_view(actions={'get':'retrieve'})
        god_test2 = GOD.objects.create(code=666,
                                       fabricant='AC/DC',
                                       port_quantity=13,
                                       site_id=sitetest)
        primary_key = god_test2.pk
        god_test2.delete()
        response = god_detail(request, pk=primary_key)
        self.assertEqual(response.status_code, 404)

    def test_godport_view_set(self):
        request = APIRequestFactory().get("")
        godport_detail = GODPortListViewSet.as_view(actions={'get':'retrieve'})
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)
        sitetype = SiteType.objects.create(description='IDK What Am I Doing')
        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        god_test = GOD.objects.create(code=1,
                                      fabricant='Potato Bread',
                                      port_quantity=4,
                                      site_id=sitetest)

        response = godport_detail(request, pk=god_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_godport_view_set(self):
        request = APIRequestFactory().get("")
        godport_detail = GODPortListViewSet.as_view(actions={'get':'retrieve'})
        tipo = GODPortConnectionType.objects.create(code="abcd")
        gbictipo = GBIC_Type.objects.create(description="testechato")
        gbic = GBIC.objects.create(serial="huehue", patrimony_number="123", gbic_type=gbictipo)
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)
        sitetype = SiteType.objects.create(description='IDK What Am I Doing')
        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        dgo = GOD.objects.create(code=198,
                                 fabricant="HotAntardida",
                                 port_quantity=42,
                                 site_id=sitetest)

        godport_test2 = GODPort.objects.create(code=999,
                                               connection_type=tipo,
                                               god_id=dgo,
                                               gbic_id=gbic)
        godport_test2.delete()
        response = godport_detail(request, pk=godport_test2.pk)
        self.assertEqual(response.status_code, 404)

    def test_godport_connection_type(self):
        request = APIRequestFactory().get("")
        god_type = GODPortConnectionTypeListViewSet.as_view(actions={'get':'retrieve'})
        godport_connection_type_test = GODPortConnectionType.objects.create(code=100)
        response = god_type(request, pk=godport_connection_type_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_godport_type(self):
        request = APIRequestFactory().get("")
        god_type = GODPortConnectionTypeListViewSet.as_view(actions={'get':'retrieve'})
        godport_connection_type_test = GODPortConnectionType.objects.create(code=100)
        godport_connection_type_test.delete()
        response = god_type(request, pk=godport_connection_type_test.pk)
        self.assertEqual(response.status_code, 404)

class JumperTest(TestCase):

    def test_jumper_view_set(self):
        request = APIRequestFactory().get("")
        jumper_detail = JumperViewSet.as_view(actions={'get':'retrieve'})
        tipo = GODPortConnectionType.objects.create(code="abcd")
        gbictipo = GBIC_Type.objects.create(description="tipoteste")
        gbic = GBIC.objects.create(serial="huehue",
                                   patrimony_number="123",
                                   gbic_type=gbictipo)
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)
        sitetype = SiteType.objects.create(description='IDK What Am I Doing')

        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        dgo = GOD.objects.create(code=198,
                                 fabricant="HotAntardida",
                                 port_quantity=42,
                                 site_id=sitetest)
        godport_test = GODPort.objects.create(code=999,
                                              connection_type=tipo,
                                              god_id=dgo,
                                              gbic_id=gbic)
        godport_test2 = GODPort.objects.create(code=109,
                                               connection_type=tipo,
                                               god_id=dgo,
                                               gbic_id=gbic)
        jumper_test = Jumper.objects.create(god_port1=godport_test, god_port2=godport_test2)
        response = jumper_detail(request, pk=jumper_test.pk)
        self.assertEqual(response.status_code, 200)

    def test_wrong_jumper_view_set(self):
        request = APIRequestFactory().get("")
        jumper_detail = JumperViewSet.as_view(actions={'get':'retrieve'})
        tipo = GODPortConnectionType.objects.create(code="abcd")
        gbictipo = GBIC_Type.objects.create(description="tipoteste")
        gbic = GBIC.objects.create(serial="huehue",
                                   patrimony_number="123",
                                   gbic_type=gbictipo)
        ipatype = InstitutionType.objects.create(description='BestEver')
        ipa = ParticipantInstitution.objects.create(name='Uns Paranauês Maneiros',
                                                    institution_type=ipatype)
        sitetype = SiteType.objects.create(description='IDK What Am I Doing')
        sitetest = Site.objects.create(
            name='Lenny Face',
            lattitude=42.42,
            longitude=54.54,
            bandwidth=42,
            ipa_code=ipa,
            site_type=sitetype
        )
        dgo = GOD.objects.create(code=198,
                                 fabricant="HotAntardida",
                                 port_quantity=42,
                                 site_id=sitetest)

        godport_test = GODPort.objects.create(code=999,
                                              connection_type=tipo,
                                              god_id=dgo,
                                              gbic_id=gbic)

        godport_test2 = GODPort.objects.create(code=109,
                                               connection_type=tipo,
                                               god_id=dgo,
                                               gbic_id=gbic)

        jumper_test = Jumper.objects.create(god_port1=godport_test, god_port2=godport_test2)
        jumper_test.delete()
        response = jumper_detail(request, pk=jumper_test.pk)
        self.assertEqual(response.status_code, 404)


class AccessCableTest(TestCase):

    def test_acess_cable_view_set(self):
        request = APIRequestFactory().get("")
        view = AccessCableListViewSet.as_view(actions={'get': 'retrieve'})
        site_type = SiteType.objects.create(description="RandomSiteType")
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB',
                                                    institution_type=instituion_type)

        site = Site.objects.create(name='RandomSite',
                                   lattitude=42,
                                   longitude=42,
                                   bandwidth=42,
                                   ipa_code=ipa,
                                   site_type=site_type)

        god = GOD.objects.create(code=1,
                                 fabricant="FabricanteTeste",
                                 port_quantity="10",
                                 site_id=site)

        access_cable = AccessCable.objects.create(cod=1,
                                                  length=120,
                                                  fiber_quantity=10,
                                                  god_id=god,
                                                  site_id=site)

        response = view(request, pk=access_cable.pk)
        self.assertEqual(response.status_code, 200)

    def test_access_cable_post(self):
        view = AccessCableListViewSet.as_view(actions={'get': 'list'})
        factory = APIRequestFactory()
        site_type = SiteType.objects.create(description="RandomSiteType")
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB', institution_type=instituion_type)
        site = Site.objects.create(name='RandomSite',
                                   lattitude=42,
                                   longitude=42,
                                   bandwidth=42,
                                   ipa_code=ipa,
                                   site_type=site_type)

        god = GOD.objects.create(code=1,
                                 fabricant="FabricanteTeste",
                                 port_quantity="10",
                                 site_id=site)
        AccessCable.objects.create(cod=1,
                                   length=120,
                                   fiber_quantity=10,
                                   god_id=god,
                                   site_id=site)
        request = factory.get('/access-cables/?all=1')
        response = view(request)
        items = response.data[0]
        self.assertEqual(list(items.values())[1], 120)
