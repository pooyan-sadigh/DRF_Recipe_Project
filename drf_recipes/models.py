import uuid
import os

from django.db import models
from django.conf import settings
from DRF1.settings import MEDIA_ROOT


def recipe_image_file_path(instance, filename):
    """generate file path for new recipe image"""

    ext = filename.split('.')[-1]
    filename = os.path.join(MEDIA_ROOT, f"{uuid.uuid4()}.{ext}")
    return filename


class Recipe(models.Model):
    """recipe object"""

    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_min = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('drf_ingredients.Ingredient')
    tags = models.ManyToManyField('drf_tags.Tag')
    image = models.ImageField(upload_to=recipe_image_file_path, default=os.path.join(MEDIA_ROOT, "default.jpeg"))

    def __str__(self):
        return self.title
