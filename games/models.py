# games.models
import uuid
from django.db import models
from gamerooms.models import Gameroom

class Game(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['gameroom']),
        ]

    gameId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gameMul = models.FloatField(default=2)
    gameDiv = models.FloatField(default=3)
    gameMin = models.IntegerField(default=1)
    gameMax = models.IntegerField(default=100)
    gameStart = models.DateTimeField()
    gameEnd = models.DateTimeField()
    gameroom = models.ForeignKey(Gameroom, on_delete=models.CASCADE, )
