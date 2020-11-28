import graphene

from restaurant_entities.models.menu import Language
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.language import (
    LanguageList,
    LanguageNode, LanguageInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.language import LanguageForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    languages = graphene.Field(LanguageList)
    language = graphene.Field(LanguageNode, id=graphene.ID(required=True))

    def resolve_language(self, info, id):
        return Language.objects.get(gid=id)

    def resolve_languages(self, info, **kwargs):
        qs = Language.objects.all()
        return LanguageList(qs)


class CreateLanguageMutation(graphene.Mutation):
    class Arguments:
        input = LanguageInput(
            required=True,
            description="Fields required to create a language."
        )

    language = graphene.Field(
        LanguageNode,
        description='Created language.'
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a language."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        form = LanguageForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateLanguageMutation(
                errors=get_errors(form.errors)
            )
        language = form.save()

        return CreateLanguageMutation(
            language=language
        )


class Mutation(graphene.ObjectType):
    create_language = CreateLanguageMutation.Field()
