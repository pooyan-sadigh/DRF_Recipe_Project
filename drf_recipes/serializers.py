from rest_framework import serializers

from .models import Recipe
from drf_ingredients.models import Ingredient
from drf_ingredients.serializers import IngredientSerializer
from drf_tags.models import Tag
from drf_tags.serializers import TagSerializer


class RecipeSerializer(serializers.ModelSerializer):
    """serializer for recipe object"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_min', 'price', 'ingredients', 'tags', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """serialize a recipe detail"""

    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)


class RecipeImageSerializer(serializers.ModelSerializer):
    """serializer for uploading images of recipes"""

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)
