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


class CategoryTranslationList(graphene.ObjectType):
    data = graphene.List(CategoryTranslationNode)


class CategoryTranslationInput(graphene.InputObjectType):
    category = graphene.String()
    language = graphene.String()
    name = graphene.String()
