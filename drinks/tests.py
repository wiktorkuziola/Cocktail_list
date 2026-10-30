from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Ingredient, Cocktail
# Create your tests here.
class CocktailAPITests(APITestCase):
    def setUp(self):
        # Przygotowujemy dane testowe przed każdym testem
        self.mint = Ingredient.objects.create(
            name="Mięta", description="Świeże listki", is_alcoholic=False
        )
        self.vodka = Ingredient.objects.create(
            name="Wódka", description="Czysty alkohol", is_alcoholic=True
        )

    def test_create_cocktail_with_ingredients(self):
        """Test sprawdzający tworzenie koktajlu wraz z proporcjami składników (POST)"""
        data = {
            "name": "Mojito",
            "category": "Orzeźwiające",
            "instruction": "Wymieszaj składniki.",
            "recipe_items": [
                {"ingredient": self.mint.id, "amount": "5 listków"},
                {"ingredient": self.vodka.id, "amount": "40 ml"}
            ]
        }
        response = self.client.post('/api/cocktails/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cocktail.objects.count(), 1)
        self.assertEqual(len(response.data['recipe_items']), 2)

    def test_filter_non_alcoholic_cocktails(self):
        """Test sprawdzający filtrowanie koktajli bezalkoholowych"""
        # Tworzymy drink alkoholowy i bezalkoholowy
        self.client.post('/api/cocktails/', {
            "name": "Drink z prądem", "category": "Mocne", "instruction": "...",
            "recipe_items": [{"ingredient": self.vodka.id, "amount": "50 ml"}]
        }, format='json')
        self.client.post('/api/cocktails/', {
            "name": "Lemoniada miętowa", "category": "Lato", "instruction": "...",
            "recipe_items": [{"ingredient": self.mint.id, "amount": "10 listków"}]
        }, format='json')

        # Pytamy API tylko o koktajle bezalkoholowe
        response = self.client.get('/api/cocktails/?is_alcoholic=false')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], "Lemoniada miętowa")