from .views import UplinkViewSet

uplinklist = UplinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

uplinkdetail = UplinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
