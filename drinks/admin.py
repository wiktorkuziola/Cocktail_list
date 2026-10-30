
# Register your models here.
from django.contrib import admin
from .models import Ingredient, Cocktail, CocktailIngredient

admin.site.register(Ingredient)
admin.site.register(Cocktail)
admin.site.register(CocktailIngredient)