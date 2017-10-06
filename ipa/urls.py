from .views import SiteListViewSet, SiteTypeListViewSet
from .views import SwitchViewSet
# from rest_framework import renderers

site = SiteListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

site_detail = SiteListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

sitetype = SiteTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

switch = SwitchViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
