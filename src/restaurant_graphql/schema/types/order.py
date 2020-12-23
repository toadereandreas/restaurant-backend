from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.order import Order, Serving
import redis

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

    def resolve_locked(self, info):

        redis_instance = redis.StrictRedis(host='localhost',
                                           port=6379, db=0)

        # print(str(self.id),"redis",len(str(redis_instance.get(str(self.id))))," apoi ",str(redis_instance.get(str(self.id)))=="b'True'")
        if str(redis_instance.get(self.id)) == "b'True'":
            return True
        return False
        # return redis_instance.get(str(self.id))


class OrderList(graphene.ObjectType):
    data = graphene.List(OrderNode)


class OrderInput(graphene.InputObjectType):
    serving = graphene.String()
    color = graphene.String()
    note = graphene.String()


class SetLockedInput(graphene.InputObjectType):
    locked = graphene.Boolean()
