from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Group, Follow
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )
        return queryset.comments


@action(detail=False, methods=('post',))
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@action(detail=False, methods=('post',))
class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
