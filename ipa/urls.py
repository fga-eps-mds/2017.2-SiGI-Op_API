from .views import SiteListViewSet, SiteTypeListViewSet
# from rest_framework import renderers

site = SiteListViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

sitetype = SiteTypeListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
