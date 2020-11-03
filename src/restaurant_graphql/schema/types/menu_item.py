from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import MenuItem


class MenuItemNode(RestaurantObjectType):
    class Meta:
        model = MenuItem
        fields = [
            'gid',
            'internal_name',
            'picture',
            'price',
            'allergens'
        ]


class MenuItemList(graphene.ObjectType):
    data = graphene.List(MenuItemNode)


class MenuItemInput(graphene.InputObjectType):
    internal_name = graphene.String()
    # picture = graphene.String()
    picture = graphene.Field(lambda: ImageField)
    price = graphene.Decimal()
    allergens = graphene.String()