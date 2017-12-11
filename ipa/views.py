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
    class_name = ParticipantInstitution
    order_param_name = 'name'
    queryset = ParticipantInstitution.objects.all().order_by('name')
    serializer_class = ParticipantInstitutionSerializer


class IpaTypeListViewSet(CustomViewSet):
    class_name = InstitutionType
    order_param_name = 'description'
    queryset = InstitutionType.objects.all().order_by('description')
    serializer_class = ParticipantInstitutionTypeSerializer


class SiteListViewSet(CustomViewSet):
    class_name = Site
    order_param_name = 'name'
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer


class SiteTypeListViewSet(CustomViewSet):
    class_name = SiteType
    order_param_name = 'description'
    queryset = SiteType.objects.all().order_by('description')
    serializer_class = SiteTypeSerializer


class ContactViewSet(CustomViewSet):
    class_name = Contact
    order_param_name = 'name'
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer


class ContactTypeViewSet(CustomViewSet):
    class_name = ContactType
    order_param_name = 'description'
    queryset = ContactType.objects.all().order_by('description')
    serializer_class = ContactTypeSerializer


class GeneratorListViewSet(CustomViewSet):
    class_name = Generator
    order_param_name = 'site_id'
    queryset = Generator.objects.all().order_by('site_id')
    serializer_class = GeneratorSerializer


class NoBreakViewSet(CustomViewSet):
    class_name = NoBreak
    order_param_name = 'site_id'
    queryset = NoBreak.objects.all().order_by('site_id')
    serializer_class = NoBreakSerializer


class SwitchViewSet(CustomViewSet):
    class_name = Switch
    order_param_name = 'site_id'
    queryset = Switch.objects.all().order_by('site_id')
    serializer_class = SwitchSerializer


class GroupViewSet(CustomViewSet):
    class_name = Group
    order_param_name = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(CustomViewSet):
    class_name = Permission
    order_param_name = 'codename'
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(CustomViewSet):
    class_name = User
    order_param_name = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SlotViewSet(CustomViewSet):
    class_name = Slot
    order_param_name = 'serie'
    queryset = Slot.objects.all().order_by('serie')
    serializer_class = SlotSerializer


class SlotPortViewSet(CustomViewSet):
    class_name = SlotPort
    order_param_name = 'port_type'
    queryset = SlotPort.objects.all().order_by('port_type')
    serializer_class = SlotPortSerializer
