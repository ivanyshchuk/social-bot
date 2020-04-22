from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls import url

from user.views import UserActivityView, CreateUserView, TokenAuthenticationView

urlpatterns = [
    url('activity/', UserActivityView.as_view({'get': 'list'}), name='user-activity'),
    url('sing-up/', CreateUserView.as_view(), name='user-sing-up'),
    url('login/', TokenAuthenticationView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
