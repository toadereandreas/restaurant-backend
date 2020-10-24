import graphene
from graphene_django import DjangoObjectType


class RestaurantObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    def resolve_id(self, info):
        return self.gid


class ErrorType(graphene.ObjectType):
    field = graphene.String(
        description=(
            """Name of a field that caused the error. A value of
            `__all__` indicates that the error isn't associated with a particular
            field.""")
    )
    messages = graphene.List(
        graphene.String,
        description='A list of error messages.'
    )
    errors = graphene.List('restaurant_graphql.schema.types.base.ErrorType')
