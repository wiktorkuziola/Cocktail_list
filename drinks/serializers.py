from rest_framework import serializers
from .models import Ingredient, Cocktail, CocktailIngredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description', 'is_alcoholic', 'image']

class CocktailIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = CocktailIngredient
        fields = ['ingredient', 'ingredient_name', 'amount']

class CocktailSerializer(serializers.ModelSerializer):
    recipe_items = CocktailIngredientSerializer(many=True)

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'instruction', 'recipe_items']

    def create(self, validated_data):
        items_data = validated_data.pop('recipe_items')
        cocktail = Cocktail.objects.create(**validated_data)
        for item in items_data:
            CocktailIngredient.objects.create(cocktail=cocktail, **item)
        return cocktail

    def update(self, instance, validated_data):
        items_data = validated_data.pop('recipe_items', None)
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.instruction = validated_data.get('instruction', instance.instruction)
        instance.save()

        if items_data is not None:
            instance.recipe_items.all().delete()
            for item in items_data:
                CocktailIngredient.object.create(cocktail=instance, **item)
        return instance