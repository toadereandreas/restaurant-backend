from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import Category


class CategoryNode(RestaurantObjectType):
    class Meta:
        model = Category
        fields = [
            'gid',
            'internal_name'
        ]

    id = graphene.ID()

    def resolve_id(self, info):
        return Category.get_pk(gid=self.gid)


class CategoryList(graphene.ObjectType):
    data = graphene.List(CategoryNode)


class CategoryInput(graphene.InputObjectType):
    internal_name = graphene.String()
