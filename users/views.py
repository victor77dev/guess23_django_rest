# users.views
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import UserSerializer, UserEmailSerializer, UserUsernameSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return CustomUser.objects.get(email=user)

class UserFindEmailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserEmailSerializer

    def get_object(self):
        email = self.request.GET.get('email')
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

class UserFindUsernameView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserUsernameSerializer

    def get_object(self):
        username = self.request.GET.get('username')
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None
