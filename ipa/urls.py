from ipa.views import SiteListViewSet, SiteTypeListViewSet

site = SiteListViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

sitetype = SiteTypeListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
