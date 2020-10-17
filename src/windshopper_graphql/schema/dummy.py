import graphene

from windshopper_entities.models import Dummy
from windshopper_graphql.schema.types.base import ErrorType
from windshopper_graphql.schema.types.dummy import DummyNode, DummyList, DummyInput

from windshopper_graphql.schema.helpers import get_errors
from windshopper_graphql.forms.dummy import DummyForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    dummies = graphene.Field(DummyList)
    dummy = graphene.Field(DummyNode, id=graphene.ID(required=True))

    def resolve_dummy(self, info, id):
        return Dummy.objects.get(gid=id)

    def resolve_dummies(self, info, **kwargs):
        qs = Dummy.objects.all()
        return DummyList(qs)


class CreateDummyMutation(graphene.Mutation):
    class Arguments:
        input = DummyInput(
            required=True,
            description="Fields required to create a dummy."
        )

    dummy = graphene.Field(
        DummyNode,
        description='Created dummy.'
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a dummy."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        form = DummyForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateDummyMutation(
                errors=get_errors(form.errors)
            )
        dummy = form.save()

        return CreateDummyMutation(
            dummy=dummy
        )


class Mutation(graphene.ObjectType):
    create_dummy = CreateDummyMutation.Field()
