import graphene

from .dummy import Query as DummyQuery, Mutation as DummyMutation
from .user import Query as UserQuery, Mutation as UserMutation


class Query(
    UserQuery,
    DummyQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    UserMutation,
    DummyMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
