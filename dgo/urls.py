from .views import GODListViewSet

god = GODListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
