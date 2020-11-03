from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import AllergenTranslation


class AllergenTranslationNode(RestaurantObjectType):
    class Meta:
        model = AllergenTranslation
        fields = [
            'gid',
            'name',
            'allergen',
            'language'
        ]


class AllergenTranslationList(graphene.ObjectType):
    data = graphene.List(AllergenTranslationNode)


class AllergenTranslationInput(graphene.InputObjectType):
    name = graphene.String()
    allergen = graphene.String()
    language = graphene.String()