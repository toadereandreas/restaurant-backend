import graphene

from restaurant_entities.models.menu import Category
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.category import (
    CategoryList,
    CategoryNode, CategoryInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.category import CategoryForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    categories = graphene.Field(CategoryList)
    category = graphene.Field(CategoryNode, id=graphene.ID(required=True))

    def resolve_category(self, info, id):
        return Category.objects.get(gid=id)

    def resolve_categories(self, info, **kwargs):
        qs = Category.objects.all()
        return CategoryList(qs)


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        input = CategoryInput(
            required=True,
            description="Fields required to create a category."
        )

    category = graphene.Field(
        CategoryNode,
        description='Created category.'
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a category."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        form = CategoryForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateCategoryMutation(
                errors=get_errors(form.errors)
            )
        category = form.save()

        return CreateCategoryMutation(
            category=category
        )


class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()