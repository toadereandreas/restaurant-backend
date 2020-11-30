from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.order import Order, Serving


class OrderNode(RestaurantObjectType):
    class Meta:
        model = Order
        fields = [
            'gid',
            'serving',
            'color',
            'note'
        ]

    id = graphene.ID()
    serving_id = graphene.ID()
    locked = graphene.Boolean()

    def resolve_id(self, info):
        return Order.get_pk(gid=self.gid)

    def resolve_serving_id(self, info):
        return Serving.get_pk(gid=self.serving.gid)

    def resolve_locked(self, indo):
        return False


class OrderList(graphene.ObjectType):
    data = graphene.List(OrderNode)


class OrderInput(graphene.InputObjectType):
    serving = graphene.String()
    color = graphene.String()
    note = graphene.String()
