import graphene
from rx import Observable

from restaurant_entities.models.order import  Order, OrderMenuItem, Serving
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.order_menu_item import (
    OrderMenuItemList,
    OrderMenuItemNode, OrderMenuItemInput,
)

from restaurant_graphql.schema.types.order import OrderNode
from restaurant_graphql.schema.types.serving import ServingNode

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.order_menu_item import OrderMenuItemForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    order_menu_items = graphene.Field(
        OrderMenuItemList,
        id=graphene.ID(),
    )
    order_menu_item = graphene.Field(OrderMenuItemNode, id=graphene.ID(required=True))

    def resolve_order_menu_item(self, info, id):
        return OrderMenuItem.objects.get(gid=id)

    def resolve_order_menu_items(self, info, **kwargs):
        qs = OrderMenuItem.objects.all()
        return OrderMenuItemList(qs)


class CreateOrderMenuItemMutation(graphene.Mutation):
    class Arguments:
        input = OrderMenuItemInput(
            required=True,
            description="Fields required to create a order_menu_item."
        )

    order_menu_item = graphene.Field(
        OrderMenuItemNode,
        description="Created order_menu_item."
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a order_menu_item."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # user = info.context.user
        # kwargs['input']['user'] = user
        form = OrderMenuItemForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateOrderMenuItemMutation(
                errors=get_errors(form.errors)
            )
        order_menu_item = form.save()

        return CreateOrderMenuItemMutation(
            order_menu_item=order_menu_item
        )

class DeleteOrderMenuItemMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True,description="id to delete an OrderMenuItem")
    id=graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        order_menu_item = OrderMenuItem.objects.get(gid=id)
        order_menu_item.delete()

        return DeleteOrderMenuItemMutation(
            id=id
        )
    
class UpdateOrderMenuItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="id to update an OrderMenuItem")
        input = OrderMenuItemInput(
            required = True,
            description = "Fields required to create an OrderMenuItem."
        )

    order_menu_item = graphene.Field(
        OrderMenuItemNode,
        description = "Updated OrderMenuItem."
    )

    errors = graphene.List(
        ErrorType,
        description = 'List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Updates an OrderMenuItem."

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        order_menu_item=OrderMenuItem.objects.get(gid=id)
        form = OrderMenuItemForm(data=kwargs['input'], instance=order_menu_item)

        if not form.is_valid():
            return UpdateOrderMenuItemMutation(
                errors = get_errors(form.errors)
            )
        order_menu_item = form.save()

        return UpdateOrderMenuItemMutation(
            order_menu_item=order_menu_item
        )

class Mutation(graphene.ObjectType):
    create_order_menu_item = CreateOrderMenuItemMutation.Field()
    delete_order_menu_item=DeleteOrderMenuItemMutation.Field()
    update_order_menu_item=UpdateOrderMenuItemMutation.Field()
