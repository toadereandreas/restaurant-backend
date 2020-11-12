import django_filters

from restaurant_entities.models import MenuItem
from .base import RestaurantFilter


class MenuFilter(RestaurantFilter):
    id = django_filters.CharFilter(
        field_name='gid',
        lookup_expr='icontains',
    )
    category_name = django_filters.CharFilter(
        field_name='category__internal_name'
    )
    order_by = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),
        )
    )

    class Meta:
        model = MenuItem
        fields = []
