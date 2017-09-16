from underground_box.views import UndergroundBoxViewSet,api_root
from rest_framework import renderers

undergroundboxlist = UndergroundBoxViewSet.as_view({
    'get' : 'list',
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
