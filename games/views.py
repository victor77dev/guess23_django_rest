# games.views
from rest_framework import generics

from .models import Game
from .serializers import GameSerializer

class GameListCreateView(generics.ListCreateAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        return Game.objects.all()
