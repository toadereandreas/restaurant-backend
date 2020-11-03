import graphene

from restaurant_entities.models.menu import CategoryTranslation
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.category_translation import (
    CategoryTranslationList,
    CategoryTranslationNode, CategoryTranslationInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.category_translation import CategoryTranslationForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    category_translations = graphene.Field(CategoryTranslationList)
    category_translation = graphene.Field(CategoryTranslationNode, id=graphene.ID(required=True))

    def resolve_category_translation(self, info, id):
        return CategoryTranslation.objects.get(gid=id)

    def resolve_category_translations(self, info, **kwargs):
        qs = CategoryTranslation.objects.all()
        return CategoryTranslationList(qs)

