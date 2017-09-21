from rest_framework.viewsets import ModelViewSet
from contact import models, serializers
# Create your views here.


class ContactViewSet(ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ContactTypeViewSet(ModelViewSet):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
