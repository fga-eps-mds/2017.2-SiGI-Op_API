from .views import CableStretchListViewSet
from .views import TubelooseListViewSet

cable_stretch = CableStretchListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

cable_stretch_detail = CableStretchListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

tubeloose = TubelooseListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
