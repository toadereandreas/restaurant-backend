from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.order import Serving
from restaurant_entities.users.models import CustomUser


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

    # id = graphene.ID()
    # user_id = graphene.ID()
    #
    # def resolve_id(self, info):
    #     return Serving.get_pk(gid=self.gid)
    #
    # def resolve_user_id(self, info):
    #     return CustomUser.objects.get(username=self.user.username).pk


class ServingList(graphene.ObjectType):
    data = graphene.List(ServingNode)


class ServingInput(graphene.InputObjectType):
    code = graphene.String()
    user = graphene.String()
    name = graphene.String()
    called = graphene.Boolean()
