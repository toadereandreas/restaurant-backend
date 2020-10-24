import graphene

from .dummy import Query as DummyQuery, Mutation as DummyMutation
from .user import Query as UserQuery, Mutation as UserMutation
# from graphql_auth.schema import UserQuery, MeQuery

class Query(
    UserQuery,
    DummyQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    DummyMutation,
    UserMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
