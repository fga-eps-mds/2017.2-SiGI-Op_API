from .views import GODListViewSet, GODPortListViewSet
from .views import GODPortConnectionTypeListViewSet

GOD = GODListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

GOD_PORT = GODPortListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

GOD_PORT_CONNECTION_TYPE = GODPortConnectionTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
