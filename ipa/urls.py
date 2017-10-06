from .views import SiteListViewSet, SiteTypeListViewSet
from .views import NoBreakViewSet

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

nobreak = NoBreakViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
