from django.db import models
import uuid


class Sector(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    name = models.CharField(max_length=10)
    code = models.PositiveIntegerField()
