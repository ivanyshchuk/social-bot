from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.timezone import now

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """
    create new user
    """
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class TokenAuthenticationView(TokenObtainPairView):
    """
    implementation of ObtainAuthToken with last_login update
    """
    def post(self, request):
        result = super(TokenAuthenticationView, self).post(request)
        user_id = AccessToken(result.data['access'])['user_id']
        User.objects.filter(pk=user_id).update(last_login=now())
        return result


class UserActivityView(viewsets.ModelViewSet):
    """
    return user data
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', self.request.user.pk)
        queryset = User.objects.filter(pk=user)
        return queryset
