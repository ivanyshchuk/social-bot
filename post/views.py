from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostSerializer, PostLikeSerializer, PostLikeAnaliticSerializer
from post.models import Post, PostLike


class PostView(viewsets.ModelViewSet):
    """
    return list of posts and create new post
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeView(CreateAPIView):
    """
    create post like
    """
    model = PostLike
    permission_classes = (IsAuthenticated,)
    serializer_class = PostLikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeRemove(APIView):
    """
    remove post like
    """
    def post(self, request, format=None):
        post_id = request.query_params.get('post')
        try:
            post_like = PostLike.objects.get(post_id=post_id, user=request.user)
        except PostLike.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikeAnalyticsView(viewsets.ModelViewSet):
    """
    return post like analytics
    """
    queryset = PostLike.objects.all()
    serializer_class = PostLikeAnaliticSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = PostLike.objects.all().extra({'created': "date(created)"}).values('created').annotate(
            created_count=Count('id'))
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        if date_from and date_to:
            queryset = queryset.filter(created__range=[date_from, date_to])
        return queryset
