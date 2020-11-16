from .base import RestaurantObjectType
import graphene
from restaurant_entities.models import Table


class TableNode(RestaurantObjectType):
    class Meta:
        model = Table
        fields = [
            'gid',
            'name',
            'code'
        ]


class TableList(graphene.ObjectType):
    data = graphene.List(TableNode)


class TableInput(graphene.InputObjectType):
    table_code = graphene.String()
