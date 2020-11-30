import graphene
from rx import Observable

from restaurant_entities.models.order import Order
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.order import (
    OrderList,
    OrderNode, OrderInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.order import OrderForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    orders = graphene.Field(
        OrderList,
        id=graphene.ID(),
    )
    order = graphene.Field(OrderNode, id=graphene.ID(required=True))

    def resolve_order(self, info, id):
        return Order.objects.get(gid=id)

    def resolve_orders(self, info, **kwargs):
        qs = Order.objects.all()
        return OrderList(qs)

class Subscription(graphene.ObjectType):
    orders = graphene.Field(OrderList)
    order_created = graphene.Field(OrderNode)

    def resolve_orders(root, info):
        return Observable.interval(3000).map(lambda i: orders)

    def resolve_order_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Order)
        ).map(lambda event: event.instance)
