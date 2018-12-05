# gamerooms.serializers
from rest_framework import serializers
from .models import Gameroom
from games.serializers import GameSerializer

class GameroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gameroom
        fields = ('gameroomId', 'defaultDuration')
