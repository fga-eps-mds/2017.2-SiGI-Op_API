from .views import PostListViewSet


post = PostListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = PostListViewSet.as_view({
    'get': 'list',
    'patch': 'partial_update',
    'put': 'update',
    'delete': 'destroy',
})
