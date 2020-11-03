import graphene

from .dummy import Query as DummyQuery, Mutation as DummyMutation
from .language import Query as LanguageQuery, Mutation as LanguageMutation
from .user import Query as UserQuery, Mutation as UserMutation
# from graphql_auth.schema import UserQuery, MeQuery

class Query(
    UserQuery,
    DummyQuery,
    LanguageQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    DummyMutation,
    UserMutation,
    LanguageMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
