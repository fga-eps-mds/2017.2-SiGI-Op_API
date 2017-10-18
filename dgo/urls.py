from .views import GODListViewSet, GODPortListViewSet
from .views import GODPortConnectionTypeListViewSet, JumperViewSet

god = GODListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

god_port = GODPortListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

god_port_connection_type = GODPortConnectionTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

jumper = JumperViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
