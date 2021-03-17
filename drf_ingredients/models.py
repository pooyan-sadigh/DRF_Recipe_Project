from django.db import models
from django.conf import settings


class Ingredient(models.Model):
    """ingredient used in recipe"""

    name = models.CharField(max_length=255)
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
