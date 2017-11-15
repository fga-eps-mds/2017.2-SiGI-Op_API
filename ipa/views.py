from rest_framework import viewsets
from .serializers import ParticipantInstitutionSerializer
from .serializers import ParticipantInstitutionTypeSerializer
from .serializers import ContactSerializer
from .serializers import ContactTypeSerializer, GeneratorSerializer
from .models import InstitutionType, ParticipantInstitution, Site, SiteType
from .models import Contact, ContactType, Generator
from .serializers import SwitchSerializer
from .serializers import NoBreakSerializer
from .serializers import SlotSerializer
from .serializers import SlotPortSerializer
from .models import NoBreak
from .models import Switch
from .models import Slot
from .models import SlotPort
from sigi_op.serializers import SiteTypeSerializer, SiteSerializer
from django.contrib.auth.models import User, Group, Permission
from .serializers import GroupSerializer, PermissionSerializer
from sigi_op.serializers import UserSerializer

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


class GeneratorListViewSet(viewsets.ModelViewSet):
    queryset = Generator.objects.all()
    serializer_class = GeneratorSerializer


class NoBreakViewSet(viewsets.ModelViewSet):
    queryset = NoBreak.objects.all()
    serializer_class = NoBreakSerializer


class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    def create(self, request):
        slot_data = {
            'serie': request.data['serie'],
            'number': request.data['number'],
            'patrimony': request.data['patrimony'],
            'band': request.data['band'],
            'switch_id': request.data['switch_id']
        }
        serializer = SlotSerializer(data=slot_data)
        if(serializer.is_valid()):
            slot_port_quantity = request.data['slot_port_quantity']
            number = request.data['number']
            slot_list = []
            for i in range(slot_port_quantity):
                slot_list.append(SlotPort(slot_id=serializer.id))
            SlotPort.objects.bulk_create(slot_list) 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlotPortViewSet(viewsets.ModelViewSet):
    queryset = SlotPort.objects.all()
    serializer_class = SlotPortSerializer
