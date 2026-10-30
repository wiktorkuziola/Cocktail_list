import django_filters
from .models import Cocktail

class CocktailFilter(django_filters.FilterSet):
    is_alcoholic = django_filters.BooleanFilter(method='filter_is_alcoholic', label='Czy koktajl jest alkoholowy?')
    ingredient_name = django_filters.CharFilter(field_name='ingredients__name', lookup_expr='icontains', label='Nazwa składnika zawiera')

    class Meta:
        model = Cocktail
        fields = ['category', 'ingredients', 'is_alcoholic', 'ingredient_name']

    def filter_is_alcoholic(self, queryset, name, value):
        if value is True:
            return queryset.filter(ingredients__is_alcoholic=True).distinct()
        elif value is False:
            return queryset.exclude(ingredients__is_alcoholic=True).distinct()
        return queryset