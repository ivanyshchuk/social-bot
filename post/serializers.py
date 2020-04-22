from rest_framework import serializers

from post.models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'text')


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = PostLike
        fields = ('post', 'user', 'created')


class PostLikeAnaliticSerializer(serializers.ModelSerializer):
    created_count = serializers.IntegerField()
    created = serializers.DateField()

    class Meta:
        model = PostLike
        fields = ('created_count', 'created')
