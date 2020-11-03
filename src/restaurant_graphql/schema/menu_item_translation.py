import graphene

from restaurant_entities.models.menu import MenuItemTranslation
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.menu_item_translation import (
    MenuItemTranslationList,
    MenuItemTranslationNode, MenuItemTranslationInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.menu_item_translation import MenuItemTranslationForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    menu_item_translations = graphene.Field(MenuItemTranslationList)
    menu_item_translation = graphene.Field(MenuItemTranslationNode, id=graphene.ID(required=True))

    def resolve_menu_item_translation(self, info, id):
        return MenuItemTranslation.objects.get(gid=id)

    def resolve_menu_item_translations(self, info, **kwargs):
        qs = MenuItemTranslation.objects.all()
        return MenuItemTranslationList(qs)