from .base import WindShopperObjectType
import graphene
from windshopper_entities.models import Dummy


class DummyNode(WindShopperObjectType):
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