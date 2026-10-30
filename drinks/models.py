from django.db import models

# Create your models here.
class Ingredient(models.Model):#klasa bazowa składników (tabela)
    name = models.CharField(max_length=200)#zmienna mówiąca o nazwie składnikiu
    description = models.TextField()#zmienna mówiąca o opisie składniku
    is_alcoholic = models.BooleanField(default=True)#zmienna t/f czy skladnik jest alkoholowy
    image = models.URLField(blank=True, null=True)#zmienna do zdj skladniku
    def __str__(self):
        return self.name

class Cocktail(models.Model):#klasa bazowa drinku (tabela)
    name = models.CharField(max_length=200)#zmienna mowiaca o nazwie koktajlu
    category = models.CharField(max_length=200)#zmienna mowiaca o kategorii koktajlu
    instruction = models.TextField()#zmienna mówiąca o przepisie na koktajl
    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredient')#zmienna łącząca koktajl i skladniki i aby zapisywala to w klasie CocktailIngredient
    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='recipe_items')#zapisanie klucza do klasy koktajli
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)#zapisanie klucza do klasy skladnikow
    amount = models.CharField(max_length=50)#zmienna mowiaca o ilosci




