from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import InstitutionType, Generator
from .models import ParticipantInstitution
from .models import SiteType
from .models import Site
from .models import ContactType
from .models import Contact
from .models import NoBreak
from .models import Switch
from .models import Slot
from .models import SlotPort
from technical_reserve.models import TechnicalReserve
from technical_reserve.views import TechnicalReserveListViewSet
from dgo.models import GOD
from .views import IpaTypeListViewSet, GeneratorListViewSet
from .views import IpaListViewSet
from .views import SiteTypeListViewSet
from .views import SiteListViewSet
from .views import ContactTypeViewSet
from .views import ContactViewSet
from .views import NoBreakViewSet
from .views import SwitchViewSet
from .views import SlotViewSet
from .views import SlotPortViewSet
# from technical_reserve.views import TechnicalReserveListViewSet

# Create your tests here.


class ViewSetTest(TestCase):
    def test_institution_type_view_set(self):
        request = APIRequestFactory().get("")
        view = IpaTypeListViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(
            description="RandomInstitution")

        response = view(request, pk=instituion_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_ipa_view_set(self):
        request = APIRequestFactory().get("")
        view = IpaListViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(
            description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(
            name='UnB', institution_type=instituion_type)

        response = view(request, pk=ipa.pk)
        self.assertEqual(response.status_code, 200)

    def test_technical_reserve_view_set(self):
        request = APIRequestFactory().get("")
        view = TechnicalReserveListViewSet.as_view(actions={'get': 'retrieve'})
        technica_reserve = TechnicalReserve.objects.create(code=999, length=15, lattitude=123.2, longitude=421.6)
        response = view(request, pk=technica_reserve.pk)
        self.assertEqual(response.status_code, 200)

    def test_site_type_view_set(self):
        request = APIRequestFactory().get("")
        view = SiteTypeListViewSet.as_view(actions={'get': 'retrieve'})
        site_type = SiteType.objects.create(description="RandomSiteType")

        response = view(request, pk=site_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_site_view_set(self):
        request = APIRequestFactory().get("")
        view = SiteTypeListViewSet.as_view(actions={'get': 'retrieve'})
        site_type = SiteType.objects.create(description="RandomSiteType")
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB', institution_type=instituion_type)

        site = Site.objects.create(name='RandomSite', lattitude=42, longitude=42, bandwidth=42, ipa_code=ipa, site_type=site_type)

        response = view(request, pk=site.pk)
        self.assertEqual(response.status_code, 200)

    def test_contact_type_view_set(self):
        request = APIRequestFactory().get("")
        view = ContactTypeViewSet.as_view(actions={'get': 'retrieve'})
        contact_type = ContactType.objects.create(description="RandomContactType")

        response = view(request, pk=contact_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_set(self):
        request = APIRequestFactory().get("")
        view = ContactViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB', institution_type=instituion_type)
        contact_type = ContactType.objects.create(description="RandomContactType")
        contact = Contact.objects.create(name='john', phone_number='99999999', email='john@smith.com', priority=1, contact_type=contact_type, ipa_code=ipa)

        response = view(request, pk=contact.pk)
        self.assertEqual(response.status_code, 200)

    def test_generator_view_set(self):
        request = APIRequestFactory().get("")
        view = GeneratorListViewSet.as_view(actions={'get': 'retrieve'})
        site_type = SiteType.objects.create(description="RandomSiteType")
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(
            name='UnB', institution_type=instituion_type)
        site = Site.objects.create(name='RandomSite', lattitude=42, longitude=42, bandwidth=42, ipa_code=ipa, site_type=site_type)
        generator = Generator.objects.create(power=123.3, manufacturer='Fabricante1', patrimony='Patrimonio1', site=site)
        response = view(request, pk=generator.pk)
        self.assertEqual(response.status_code, 200)
    def test_no_break_view_set(self):
        request = APIRequestFactory().get("")
        view = NoBreakViewSet.as_view(actions={'get': 'retrieve'})
        site_type = SiteType.objects.create(description="RandomSiteType")
        instituion_type = InstitutionType.objects.create(description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB', institution_type=instituion_type)
        site = Site.objects.create(name='RandomSite', lattitude=42, longitude=42, bandwidth=42, ipa_code=ipa, site_type=site_type)
        no_break = NoBreak.objects.create(power=1, proprietary='john', patrimony_number='01', site_id=site)

        response = view(request, pk=no_break.pk)
        self.assertEqual(response.status_code, 200)

    def test_switch_view_set(self):
        request = APIRequestFactory().get("")
        view = SwitchViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(
                                            description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB',
                                            institution_type=instituion_type)
        site_type = SiteType.objects.create(description="RandomSiteType")
        site_id = Site.objects.create(name='RandomSite',
                                      lattitude=42,
                                      longitude=42,
                                      bandwidth=42,
                                      ipa_code=ipa,
                                      site_type=site_type)
        switch = Switch.objects.create(serial_number='AAAAA11111',
                                       manufacturer='RandomManufacturer',
                                       slots_quantity='500',
                                       patrimony_number='AAAAA11111',
                                       site_id=site_id)
        response = view(request, pk=switch.pk)
        self.assertEqual(response.status_code, 200)

    def test_slot_view_set(self):
        request = APIRequestFactory().get("")
        view = SlotViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(
                                            description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB',
                                            institution_type=instituion_type)
        site_type = SiteType.objects.create(description="RandomSiteType")
        site_id = Site.objects.create(name='RandomSite',
                                      lattitude=42,
                                      longitude=42,
                                      bandwidth=42,
                                      ipa_code=ipa,
                                      site_type=site_type)
        switch = Switch.objects.create(serial_number='AAAAA11111',
                                       manufacturer='RandomManufacturer',
                                       slots_quantity='500',
                                       patrimony_number='AAAAA11111',
                                       site_id=site_id)
        slot = Slot.objects.create(serie='AAAAA11111',
                                   number=1,
                                   patrimony='500',
                                   port_quantity=3,
                                   band = 2,
                                   switch_id=switch)
        response = view(request, pk=slot.pk)
        self.assertEqual(response.status_code, 200)

    def test_slot_port_view_set(self):
        request = APIRequestFactory().get("")
        view = SlotPortViewSet.as_view(actions={'get': 'retrieve'})
        instituion_type = InstitutionType.objects.create(
                                            description="RandomInstitution")
        ipa = ParticipantInstitution.objects.create(name='UnB',
                                            institution_type=instituion_type)
        site_type = SiteType.objects.create(description="RandomSiteType")
        site_id = Site.objects.create(name='RandomSite',
                                      lattitude=42,
                                      longitude=42,
                                      bandwidth=42,
                                      ipa_code=ipa,
                                      site_type=site_type)
        switch = Switch.objects.create(serial_number='AAAAA11111',
                                       manufacturer='RandomManufacturer',
                                       slots_quantity='500',
                                       patrimony_number='AAAAA11111',
                                       site_id=site_id)
        slot = Slot.objects.create(serie='AAAAA11111',
                                   number=1,
                                   patrimony='500',
                                   port_quantity=3,
                                   band = 2,
                                   switch_id=switch)
        slot_port = SlotPort.objects.create(type='AAAAA11111',
                                            port='1',
                                            slot_id=slot)
        response = view(request, pk=slot_port.pk)
        self.assertEqual(response.status_code, 200)
