from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
