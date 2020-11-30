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

class Subscription(graphene.ObjectType):
    order_menu_items = graphene.Field(OrderMenuItemList, order_id=graphene.ID())
    order_menu_items_serving = graphene.Field(OrderMenuItemList, serving_id=graphene.ID())
    # order_menu_items_order = graphene.Field(OrderMenuItemList, order_id=graphene.ID())

    def resolve_order_menu_items(root, info, order_id):
        return Observable.interval(3000).map(lambda i: OrderMenuItemList(OrderMenuItem.objects.filter(order=Order.objects.get(pk=order_id))))

    def resolve_order_menu_items_serving(root, info, serving_id):
        return root.filter(
            lambda event:
                event.operation == UPDATED #and
                # isinstance(event.instance, OrderMenuItem) and
                # event.instance.serving.pk == int(serving_id)
        ).map(lambda event: OrderMenuItemList(OrderMenuItem.objects.all()))

    # def resolve_order_menu_items_order(root, info, order_id):
    #     return root.filter(
    #         lambda event:
    #             (event.operation == UPDATED or event.operation == CREATED) and
    #             isinstance(event.instance, OrderMenuItem) and
    #             event.instance.order.pk == int(order_id)
    #     ).map(lambda event: OrderMenuItemList(OrderMenuItem.objects.filter(order=Order.objects.get(pk=order_id))))
