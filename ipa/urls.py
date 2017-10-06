from .views import SiteListViewSet
from .views import SiteTypeListViewSet
from .views import NoBreakViewSet
from .views import SwitchViewSet

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

switch = SwitchViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
