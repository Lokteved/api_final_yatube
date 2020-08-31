from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'group', GroupViewSet)
router_v1.register(r'follow', FollowViewSet)
router_v1.register('posts/(?P<post_id>\d+)/comments', CommentViewSet)


urlpatterns = [
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('v1/', include(router_v1.urls))
]
