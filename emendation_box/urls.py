from .views import EmendationBoxListViewSet
from .views import EmendationBoxTypeListViewSet
from .views import EmendationBoxStructureListViewSet
from .views import PostListViewSet


# from rest_framework import renderers
emendation_box = EmendationBoxListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

emendation_box_detail = EmendationBoxListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

emendation_box_type = EmendationBoxTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

emendation_box_structure = EmendationBoxStructureListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

post = PostListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = PostListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
