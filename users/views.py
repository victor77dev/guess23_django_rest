# users.views
from rest_framework import generics

from .models import CustomUser
from .serializers import UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return CustomUser.objects.get(email=user)
