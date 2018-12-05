# games.models
import uuid
from django.db import models

class Game(models.Model):
    gameId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gameMul = models.FloatField(default=2)
    gameDiv = models.FloatField(default=3)
    gameMin = models.IntegerField(default=1)
    gameMax = models.IntegerField(default=100)
    gameStart = models.DateTimeField()
    gameEnd = models.DateTimeField()
