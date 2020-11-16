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

    id = graphene.ID()

    def resolve_id(self, info):
        return MenuItem.get_pk(gid=self.gid)


class MenuItemList(graphene.ObjectType):
    data = graphene.List(MenuItemNode)


class MenuItemInput(graphene.InputObjectType):
    internal_name = graphene.String()
    picture = graphene.Field(lambda: ImageField)
    price = graphene.Decimal()
    quantity = graphene.String()
    allergens = graphene.String()
    category = graphene.String()
