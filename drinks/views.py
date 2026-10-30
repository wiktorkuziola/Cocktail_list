from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingredient
from .models import Cocktail
from .serializers import CocktailSerializer
from .serializers import IngredientSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_alcoholic']  # pozwala filtrować: ?is_alcoholic=true lub false
    search_fields = ['name', 'description']  # pozwala szukać tekstu: ?search=mięta
    ordering_fields = ['name', 'id']  # pozwala sortować: ?ordering=name

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'ingredients', 'ingredients__is_alcoholic']# pozwala filtrowac po kategorii itd
    search_fields = ['name', 'instruction', 'ingredients__name']#pozwala szukac tekstu
    ordering_fields = ['name', 'category', 'id']#pozwala sortowac