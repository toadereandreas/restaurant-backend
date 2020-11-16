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

    id = graphene.ID()

    def resolve_id(self, info):
        return AllergenTranslation.get_pk(gid=self.gid)


class AllergenTranslationList(graphene.ObjectType):
    data = graphene.List(AllergenTranslationNode)


class AllergenTranslationInput(graphene.InputObjectType):
    name = graphene.String()
    allergen = graphene.String()
    language = graphene.String()
