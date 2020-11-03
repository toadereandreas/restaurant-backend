from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import Allergen


class AllergenNode(RestaurantObjectType):
    class Meta:
        model = Allergen
        fields = [
            'gid',
            'number'
        ]


class AllergenList(graphene.ObjectType):
    data = graphene.List(AllergenNode)


class AllergenInput(graphene.InputObjectType):
    number = graphene.Int()