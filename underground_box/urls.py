from underground_box.views import UndergroundBoxViewSet,api_root
from rest_framework import renderers

underground_box_list = UndergroundBoxViewSet.as_view({
    'get' : 'list',
    'post': 'create'
    })
underground_box_detail = UndergroundBoxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })


