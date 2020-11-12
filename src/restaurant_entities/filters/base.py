import django_filters
from graphene.utils.str_converters import to_snake_case


class RestaurantFilter(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, **kwargs):
        if 'order_by' in data:
            data['order_by'] = to_snake_case(data['order_by'])
        super().__init__(data, queryset, **kwargs)
