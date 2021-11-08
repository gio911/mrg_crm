from django_filters import FilterSet, NumberFilter, CharFilter
from market.models import Product

class ProductFilter(FilterSet):
    category = NumberFilter()
    name = CharFilter()
    subcategory = NumberFilter()

    class Meta:
        model = Product
        fields = ['category', 'name', 'subcategory']