from .views import UplinkViewSet
from .views import SegmentsListViewSet

UPLINK_LIST = UplinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

UPLINK_DETAIL = UplinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

SEGMENTS_LIST = SegmentsListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

SEGMENTS_DETAIL = SegmentsListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
