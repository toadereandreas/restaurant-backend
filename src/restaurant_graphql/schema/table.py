import graphene
from rx import Observable

from restaurant_entities.models import Table
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.table import (
    TableList,
    TableNode, TableInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.table import TableForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    tables = graphene.Field(TableList)
    table = graphene.Field(TableNode, id=graphene.ID(required=True))

    def resolve_table(self, info, id):
        return Table.objects.get(gid=id)

    def resolve_tables(self, info, **kwargs):
        qs = Table.objects.all()
        return TableList(qs)


class CreateTableMutation(graphene.Mutation):
    class Arguments:
        input = TableInput(
            required=True,
            description="Fields required to create a table."
        )

    table = graphene.Field(
        TableNode,
        description='Created table.'
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a table."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        form = TableForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateTableMutation(
                errors=get_errors(form.errors)
            )
        table = form.save()

        return CreateTableMutation(
            table=table
        )


class Mutation(graphene.ObjectType):
    create_table = CreateTableMutation.Field()

from datetime import datetime

class Subscription(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return Observable.interval(3000) \
                         .map(lambda i: "hello world!" + str(datetime.now()))
