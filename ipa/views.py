from .serializers import ParticipantInstitutionSerializer
from .serializers import ParticipantInstitutionTypeSerializer
from .serializers import ContactSerializer
from .serializers import ContactTypeSerializer, GeneratorSerializer
from .models import InstitutionType, ParticipantInstitution, Site, SiteType
from .models import Contact, ContactType, Generator
from .serializers import SwitchSerializer
from .serializers import NoBreakSerializer
from .models import NoBreak
from .models import Switch
from sigi_op.serializers import SiteTypeSerializer, SiteSerializer
from sigi_op.views import CustomViewSet

# Create your views here.


class IpaListViewSet(CustomViewSet):
    queryset = ParticipantInstitution.objects.all().order_by('name')
    serializer_class = ParticipantInstitutionSerializer


class IpaTypeListViewSet(CustomViewSet):
    queryset = InstitutionType.objects.all().order_by('description')
    serializer_class = ParticipantInstitutionTypeSerializer


class SiteListViewSet(CustomViewSet):
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer


class SiteTypeListViewSet(CustomViewSet):
    queryset = SiteType.objects.all().order_by('description')
    serializer_class = SiteTypeSerializer


class ContactViewSet(CustomViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer


class ContactTypeViewSet(CustomViewSet):
    queryset = ContactType.objects.all().order_by('description')
    serializer_class = ContactTypeSerializer


class GeneratorListViewSet(CustomViewSet):
    queryset = Generator.objects.all().order_by('site_id')
    serializer_class = GeneratorSerializer


class NoBreakViewSet(CustomViewSet):
    queryset = NoBreak.objects.all().order_by('site_id')
    serializer_class = NoBreakSerializer


class SwitchViewSet(CustomViewSet):
    queryset = Switch.objects.all().order_by('site_id')
    serializer_class = SwitchSerializer
