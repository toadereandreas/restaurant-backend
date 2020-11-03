import graphene

from restaurant_entities.models.menu import AllergenTranslation
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.allergen_translation import (
    AllergenTranslationList,
    AllergenTranslationNode, AllergenTranslationInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.allergen_translation import AllergenTranslationForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    allergen_translations = graphene.Field(AllergenTranslationList)
    allergen_translation = graphene.Field(AllergenTranslationNode, id=graphene.ID(required=True))

    def resolve_allergen_translation(self, info, id):
        return AllergenTranslation.objects.get(gid=id)

    def resolve_allergen_translations(self, info, **kwargs):
        qs = AllergenTranslation.objects.all()
        return AllergenTranslationList(qs)