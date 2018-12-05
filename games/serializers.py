# games.serializers
from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    gameEnd = serializers.DateTimeField(required=False)

    class Meta:
        model = Game
        fields = ('gameId', 'gameMul', 'gameDiv', 'gameMin', 'gameMax', 'gameStart', 'gameEnd', 'gameroom')
