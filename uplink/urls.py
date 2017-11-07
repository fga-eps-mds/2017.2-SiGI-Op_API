from .views import UplinkViewSet
from .views import SegmentsListViewSet

uplinklist = UplinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

uplinkdetail = UplinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

segmentslist = SegmentsListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

segmentsdetail = SegmentsListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
