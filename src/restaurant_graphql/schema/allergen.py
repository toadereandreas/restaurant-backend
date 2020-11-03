import graphene

from restaurant_entities.models.menu import Allergen
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.allergen import (
    AllergenList,
    AllergenNode, AllergenInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.allergen import AllergenForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    allergens = graphene.Field(AllergenList)
    allergen = graphene.Field(AllergenNode, id=graphene.ID(required=True))

    def resolve_allergen(self, info, id):
        return Allergen.objects.get(gid=id)

    def resolve_allergens(self, info, **kwargs):
        qs = Allergen.objects.all()
        return AllergenList(qs)