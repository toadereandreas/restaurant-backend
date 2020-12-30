from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.order import Serving
from restaurant_entities.users.models import CustomUser
import redis

class ServingNode(RestaurantObjectType):
    class Meta:
        model = Serving
        fields = [
            'gid',
            'code',
            'user',
            'name',
            'called'
        ]

    id = graphene.ID()
    user_id = graphene.ID()
    # called = graphene.Boolean()


    def resolve_id(self, info):
        return Serving.get_pk(gid=self.gid)

    def resolve_user_id(self, info):
        return CustomUser.objects.get(username=self.user.username).pk

    # def resolve_called(self, info):
    #     #return False
    #     redis_instance = redis.StrictRedis(host='localhost',
    #                                        port=6379, db=0)
    #     if str(redis_instance.get(str(self.gid))) == "b'True'":
    #         return True
    #     return False


class ServingList(graphene.ObjectType):
    data = graphene.List(ServingNode)


class ServingInput(graphene.InputObjectType):
    code = graphene.String()
    user = graphene.String()
    name = graphene.String()
    called = graphene.Boolean()
