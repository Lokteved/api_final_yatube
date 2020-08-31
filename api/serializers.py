from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post, Comment, Group, Follow


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )

    post = serializers.IntegerField(source='post_id')

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        required=False
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Follow
