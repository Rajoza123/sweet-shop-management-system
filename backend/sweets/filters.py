import django_filters
from .models import Sweet

class SweetFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Sweet
        fields = ["category", "min_price", "max_price"]
