import graphene

from .dummy import Query as DummyQuery, Mutation as DummyMutation
from .language import Query as LanguageQuery, Mutation as LanguageMutation
from .category import Query as CategoryQuery, Mutation as CategoryMutation
from .category_translation import Query as CategoryTranslationQuery
from .allergen import Query as AllergenQuery
from .allergen_translation import Query as AllergenTranslationQuery
from .menu_item import Query as MenuItemQuery
from .menu_item_translation import Query as MenuItemTranslationQuery
from .table import Query as TableQuery
from .booking import Query as BookingQuery, Mutation as BookingMutation
from .user import Query as UserQuery, Mutation as UserMutation
from .order import Query as OrderQuery, Mutation as OrderMutation
from .order_menu_item import Query as OrderMenuItemQuery,  Mutation as OrderMenuItemMutation
from .serving import Query as ServingQuery, Mutation as ServingMutation
# from graphql_auth.schema import UserQuery, MeQuery

class Query(
    UserQuery,
    DummyQuery,
    LanguageQuery,
    CategoryQuery,
    CategoryTranslationQuery,
    AllergenQuery,
    AllergenTranslationQuery,
    MenuItemQuery,
    MenuItemTranslationQuery,
    TableQuery,
    BookingQuery,
    ServingQuery,
    OrderQuery,
    OrderMenuItemQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    DummyMutation,
    UserMutation,
    LanguageMutation,
    CategoryMutation,
    BookingMutation,
    ServingMutation,
    OrderMutation,
    OrderMenuItemMutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
