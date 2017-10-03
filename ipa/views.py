from rest_framework import viewsets
from .serializers import ParticipantInstitutionSerializer
from .serializers import ParticipantInstitutionTypeSerializer
from .serializers import ContactSerializer, ContactTypeSerializer
from .serializers import SwitchSerializer
from .models import InstitutionType, ParticipantInstitution, Site, SiteType
from .models import Contact, ContactType
from .models import Switch
from sigi_op.serializers import SiteTypeSerializer, SiteSerializer

# Create your views here.


class IpaListViewSet(viewsets.ModelViewSet):
    queryset = ParticipantInstitution.objects.all()
    serializer_class = ParticipantInstitutionSerializer


class IpaTypeListViewSet(viewsets.ModelViewSet):
    queryset = InstitutionType.objects.all()
    serializer_class = ParticipantInstitutionTypeSerializer


class SiteListViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class SiteTypeListViewSet(viewsets.ModelViewSet):
    queryset = SiteType.objects.all()
    serializer_class = SiteTypeSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
