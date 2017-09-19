from underground_box.views import UndergroundBoxViewSet
from underground_box.views import UndergroundBoxTypeViewSet

undergroundboxlist = UndergroundBoxViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })
undergroundboxdetail = UndergroundBoxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })

undergroundboxtype = UndergroundBoxTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',

    })
