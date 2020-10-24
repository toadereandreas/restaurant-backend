from .base import RestaurantObjectType
import graphene
from restaurant_entities.models import Dummy


class DummyNode(RestaurantObjectType):
    class Meta:
        model = Dummy
        fields = [
            'gid',
            'test_name',
            'test_age'
        ]


class DummyList(graphene.ObjectType):
    data = graphene.List(DummyNode)


class DummyInput(graphene.InputObjectType):
    test_name = graphene.String()
    test_age = graphene.Int()
