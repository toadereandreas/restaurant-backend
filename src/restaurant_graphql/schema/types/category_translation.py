from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import CategoryTranslation


class CategoryTranslationNode(RestaurantObjectType):
    class Meta:
        model = CategoryTranslation
        fields = [
            'gid',
            'category',
            'language',
            'name'
        ]

    id = graphene.ID()

    def resolve_id(self, info):
        return CategoryTranslation.get_pk(gid=self.gid)


class CategoryTranslationList(graphene.ObjectType):
    data = graphene.List(CategoryTranslationNode)


class CategoryTranslationInput(graphene.InputObjectType):
    category = graphene.String()
    language = graphene.String()
    name = graphene.String()
