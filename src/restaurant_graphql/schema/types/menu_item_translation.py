from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import MenuItemTranslation


class MenuItemTranslationNode(RestaurantObjectType):
    class Meta:
        model = MenuItemTranslation
        fields = [
            'gid',
            'menu_item',
            'language',
            'name',
            'description'
        ]

    id = graphene.ID()

    def resolve_id(self, info):
        return MenuItemTranslation.get_pk(gid=self.gid)

class MenuItemTranslationList(graphene.ObjectType):
    data = graphene.List(MenuItemTranslationNode)


class MenuItemTranslationInput(graphene.InputObjectType):
    menu_item = graphene.String()
    language = graphene.String()
    name = graphene.String()
    description = graphene.Field(lambda: TextField)
