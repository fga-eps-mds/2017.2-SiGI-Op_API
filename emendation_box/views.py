from rest_framework import viewsets
from .serializers import EmendationBoxSerializer
from .serializers import EmendationBoxTypeSerializer
from .serializers import EmendationBoxStructureSerializer
from .models import EmendationBoxStructure, EmendationBoxType, EmendationBox
from .serializers import PostSerializer
from .models import Post


# Create your views here.
class EmendationBoxListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBox.objects.all()
    serializer_class = EmendationBoxSerializer


class EmendationBoxTypeListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBoxType.objects.all()
    serializer_class = EmendationBoxTypeSerializer


class EmendationBoxStructureListViewSet(viewsets.ModelViewSet):
    queryset = EmendationBoxStructure.objects.all()
    serializer_class = EmendationBoxStructureSerializer


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
