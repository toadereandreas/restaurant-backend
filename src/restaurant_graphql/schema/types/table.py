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

    id = graphene.ID()

    def resolve_id(self, info):
        return Table.get_pk(gid=self.gid)


class TableList(graphene.ObjectType):
    data = graphene.List(TableNode)


class TableInput(graphene.InputObjectType):
    name = graphene.String()
    code = graphene.String()
