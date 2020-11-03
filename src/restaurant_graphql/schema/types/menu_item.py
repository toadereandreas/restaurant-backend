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
            'quantity',
            'allergens',
            'category'
        ]


class MenuItemList(graphene.ObjectType):
    data = graphene.List(MenuItemNode)


class MenuItemInput(graphene.InputObjectType):
    internal_name = graphene.String()
    # picture = graphene.String()
    picture = graphene.Field(lambda: ImageField)
    price = graphene.Decimal()
    quantity = graphene.String()
    allergens = graphene.String()
    category = graphene.String()