from sigi_op.serializers import SiteTypeSerializer, SiteSerializer
from sigi_op.serializers import UserSerializer
from sigi_op.views import CustomViewSet
from django.contrib.auth.models import User, Group, Permission
from .serializers import ParticipantInstitutionSerializer
from .serializers import ParticipantInstitutionTypeSerializer
from .serializers import ContactSerializer
from .serializers import ContactTypeSerializer, GeneratorSerializer
from .serializers import SwitchSerializer
from .serializers import NoBreakSerializer
from .serializers import SlotSerializer
from .serializers import SlotPortSerializer
from .serializers import GroupSerializer, PermissionSerializer
from .models import InstitutionType, ParticipantInstitution, Site, SiteType
from .models import Contact, ContactType, Generator
from .models import NoBreak
from .models import Switch
from .models import Slot
from .models import SlotPort

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


class GroupViewSet(CustomViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(CustomViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(CustomViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SlotViewSet(CustomViewSet):
    queryset = Slot.objects.all().order_by('serie')
    serializer_class = SlotSerializer


class SlotPortViewSet(CustomViewSet):
    queryset = SlotPort.objects.all().order_by('type')
    serializer_class = SlotPortSerializer
