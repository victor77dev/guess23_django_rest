# gamerooms.views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from .models import Gameroom
from .serializers import GameroomSerializer

class GameroomCreateView(generics.CreateAPIView):
    serializer_class = GameroomSerializer

    def create(self, request, *args, **kwargs):
        reqUser = request.user
        if reqUser.groups.filter(name='admin').exists():
            return super(GameroomCreateView, self).create(request, *args, **kwargs)
        else:
            username = reqUser.username
            userId = reqUser.id
            errMsg = "You are not allow to create gameroom as {} (userId: {}).".format(username, userId)
            return Response(
                data={
                    "error": errMsg
                },
                status=status.HTTP_404_NOT_FOUND
            )

class GameroomListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GameroomSerializer

    def get_queryset(self):
        user = self.request.user
        return Gameroom.objects.all()
