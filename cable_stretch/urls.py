from .views import CableStretchListViewSet

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
