from django.conf.urls import url, include
from rest_framework import routers

from post.views import PostLikeView, PostLikeRemove, PostLikeAnalyticsView, PostView

router = routers.DefaultRouter()
router.register(r'list', PostView, base_name='post')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^like/$', PostLikeView.as_view(), name='post-like'),
    url(r'^like-remove/$', PostLikeRemove.as_view(), name='post-like-remove'),
    url(r'^analytics/$', PostLikeAnalyticsView.as_view({'get': 'list'}), name='like-analytics'),
]
