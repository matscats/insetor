from django.db import models
import uuid


class Employee(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    name = models.CharField(max_length=50)
    sector = models.ForeignKey(
        "Sector", on_delete=models.CASCADE, related_name="employees"
    )
