from .views import EmendationBoxListViewSet
from .views import EmendationBoxTypeListViewSet
from .views import EmendationBoxStructureListViewSet


# from rest_framework import renderers
EMENDATION_BOX = EmendationBoxListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

EMENDATION_BOX_DETAIL = EmendationBoxListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

EMENDATION_BOX_TYPE = EmendationBoxTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

EMENDATION_BOX_STRUCTURE = EmendationBoxStructureListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
