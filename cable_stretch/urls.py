from .views import CableStretchListViewSet
from .views import CableStretchTypeListViewSet
from .views import TubelooseListViewSet

CABLE_STRETCH_TYPE = CableStretchTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

CABLE_STRETCH = CableStretchListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

CABLE_STRETCH_DETAIL = CableStretchListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

TUBELOOSE = TubelooseListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

TUBELOOSE_DETAIL = TubelooseListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
