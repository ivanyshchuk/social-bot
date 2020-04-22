from django.conf.urls import include, url

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^post/', include('post.urls')),
]
