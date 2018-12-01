# users.views
from rest_framework import generics

from .models import CustomUser
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(email=user)
