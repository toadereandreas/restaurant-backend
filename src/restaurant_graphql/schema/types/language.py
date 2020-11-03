from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.menu import Language


class LanguageNode(RestaurantObjectType):
    class Meta:
        model = Language
        fields = [
            'gid',
            'name',
            'code',
        ]


class LanguageList(graphene.ObjectType):
    data = graphene.List(LanguageNode)


class LanguageInput(graphene.InputObjectType):
    name = graphene.String()
    code = graphene.String()
