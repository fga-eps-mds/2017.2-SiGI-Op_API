from .views import SiteListViewSet
from .views import SiteTypeListViewSet
from .views import NoBreakViewSet
from .views import SwitchViewSet
from .views import UserViewSet, GroupViewSet, PermissionViewSet
from .views import SlotViewSet
from .views import SlotPortViewSet


SITE = SiteListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

SITE_DETAIL = SiteListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

SITE_TYPE = SiteTypeListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})

NOBREAK = NoBreakViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

SWITCH = SwitchViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})

USER = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

GROUP = GroupViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

PERMISSION = PermissionViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

SLOT = SlotViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})

SLOT_PORT = SlotPortViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
