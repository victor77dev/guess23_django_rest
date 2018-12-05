# guesses.views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from users.models import CustomUser
from .models import Guess
from .serializers import GuessSerializer

class GuessCreateView(generics.CreateAPIView):
    serializer_class = GuessSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        tokenUserId = user.id
        userId = request.data['user']
        if str(tokenUserId) == userId:
            return super(GuessCreateView, self).create(request, *args, **kwargs)
        else:
            return Response(
                data={
                    "error": "You are not allow to change userId: {} guess".format(userId)
                },
                status=status.HTTP_404_NOT_FOUND
            )

class GuessListView(generics.ListAPIView):
    serializer_class = GuessSerializer

    def get_queryset(self):
        user = self.request.user
        return Guess.objects.filter(user=user.id)

class GuessListAllView(generics.ListAPIView):
    serializer_class = GuessSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return Guess.objects.all()
