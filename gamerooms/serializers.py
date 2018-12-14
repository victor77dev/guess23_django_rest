# gamerooms.serializers
from rest_framework import serializers
from .models import Gameroom
from games.models import Game
from games.serializers import GameSerializer

class GameroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gameroom
        fields = ('gameroomId', 'defaultDuration')

class GameroomDetailSerializer(serializers.ModelSerializer):
    latestGame = serializers.SerializerMethodField()
    def get_latestGame(self, obj):
        try:
            serializedGame = GameSerializer(Game.objects.filter(gameroom=obj.gameroomId).latest('gameEnd'))
            return serializedGame.data
        except Game.DoesNotExist:
            return None

    class Meta:
        model = Gameroom
        fields = ('gameroomId', 'defaultDuration', 'latestGame')

class GameroomListGamesSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField()
    def get_games(self, obj):
        try:
            serializedGame = GameSerializer(Game.objects.filter(gameroom=obj.gameroomId).order_by('-gameEnd'), many=True)
            return serializedGame.data
        except Game.DoesNotExist:
            return None

    class Meta:
        model = Gameroom
        fields = ('gameroomId', 'defaultDuration', 'games')
