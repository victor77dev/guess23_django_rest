# guesses.serializers
from rest_framework import serializers
from .models import Guess
from games.serializers import GameSerializer
from users.serializers import CustomUser

class GuessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guess
        fields = ('id', 'game', 'user', 'guess')

class GuessDetailsSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    user = CustomUser()

    class Meta:
        model = Guess
        fields = ('id', 'game', 'user', 'guess')
