# guesses.views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from users.models import CustomUser
from .models import Guess
from games.models import Game
from .serializers import GuessSerializer, GuessDetailsSerializer

debug = True
class GuessCreateView(generics.CreateAPIView):
    serializer_class = GuessSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        tokenUserId = user.id
        userId = request.data['user']
        if str(tokenUserId) == userId:
            return super(GuessCreateView, self).create(request, *args, **kwargs)
        else:
            if debug:
                reqUser = CustomUser.objects.get(id=userId)
                errMsg = "You are not allow to change {} (userId: {}) guess".format(reqUser.username, userId)
            else:
                errMsg = "You are not allow to change userId: {} guess".format(userId)
            return Response(
                data={
                    "error": errMsg
                },
                status=status.HTTP_404_NOT_FOUND
            )

class GuessListView(generics.ListAPIView):
    serializer_class = GuessSerializer

    def get_queryset(self):
        user = self.request.user
        return Guess.objects.filter(user=user.id)

class GuessUpdateView(generics.UpdateAPIView):
    serializer_class = GuessSerializer

    def update(self, request, *args, **kwargs):
        request = self.request
        user = request.user
        tokenUserId = user.id
        userId = request.data['user']
        if str(tokenUserId) == userId:
            gameId = request.data['game']
            return super(GuessUpdateView, self).update(request, *args, **kwargs)
        else:
            if debug:
                reqUser = CustomUser.objects.get(id=userId)
                errMsg = "You are not allow to change {} (userId: {}) guess".format(reqUser.username, userId)
            else:
                errMsg = "You are not allow to change userId: {} guess".format(userId)
            return Response(
                data={
                    "error": errMsg
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def get_object(self):
        request = self.request
        user = request.user
        tokenUserId = user.id
        gameId = request.data['game']
        try:
            return Guess.objects.get(user=tokenUserId, game=gameId)
        except Guess.DoesNotExist:
            curGame = Game.objects.get(gameId=gameId)
            guessVal = request.data['guess']
            guess, created = Guess.objects.get_or_create(user=user, game=curGame, guess=guessVal)
            return guess

class GuessListAllView(generics.ListAPIView):
    serializer_class = GuessDetailsSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return Guess.objects.all()
