from .views import UndergroundBoxViewSet
from .views import UndergroundBoxTypeViewSet

UNDERGROUND_BOX_LIST = UndergroundBoxViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })
UNDERGROUND_BOX_DETAIL = UndergroundBoxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })

UNDERGROUND_BOX_TYPE = UndergroundBoxTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',

    })
