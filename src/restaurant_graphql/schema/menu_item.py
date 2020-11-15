import graphene

from restaurant_entities.models.menu import MenuItem
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.menu_item import (
    MenuItemList,
    MenuItemNode, MenuItemInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.menu_item import MenuItemForm
from graphql.error import GraphQLError

from restaurant_entities.filters.menu import MenuFilter


class Query(graphene.ObjectType):
    menu_items = graphene.Field(
        MenuItemList,
        id=graphene.ID(),
        category_name=graphene.String(),
        order_by=graphene.String(default_value='-price')
    )
    menu_item = graphene.Field(MenuItemNode, id=graphene.ID(required=True))

    def resolve_menu_item(self, info, id):
        return MenuItem.objects.get(gid=id)

    def resolve_menu_items(self, info, **kwargs):
        qs = MenuFilter(kwargs)
        return MenuItemList(qs.qs)
