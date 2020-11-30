import graphene
from rx import Observable

from restaurant_entities.models.order import Serving
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.serving import (
    ServingList,
    ServingNode, ServingInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.serving import ServingForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    servings = graphene.Field(
        ServingList,
        id=graphene.ID(),
    )
    serving = graphene.Field(ServingNode, id=graphene.ID(required=True))

    def resolve_serving(self, info, id):
        return Serving.objects.get(gid=id)

    def resolve_servings(self, info, **kwargs):
        qs = Serving.objects.all()
        return ServingList(qs)

class Subscription(graphene.ObjectType):
    servings = graphene.Field(ServingList)
    serving_created = graphene.Field(ServingNode)

    def resolve_servings(root, info):
        return Observable.interval(3000).map(lambda i: servings)

    def resolve_serving_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Serving)
        ).map(lambda event: event.instance)
