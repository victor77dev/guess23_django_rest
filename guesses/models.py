# guesses.models
from django.db import models
from users.models import CustomUser
from games.models import Game

class Guess(models.Model):
    class Meta:
        unique_together = (('game', 'user'))
        indexes = [
            models.Index(fields=['game']),
            models.Index(fields=['user']),
        ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    guess = models.IntegerField()
