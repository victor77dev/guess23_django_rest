# gamerooms.models
import uuid
from django.db import models

class Gameroom(models.Model):
    gameroomId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    defaultDuration = models.DurationField()
