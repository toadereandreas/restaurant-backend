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

import redis


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


class CreateServingMutation(graphene.Mutation):
    class Arguments:
        input = ServingInput(
            required = True,
            description = "Fields required to create a serving."
        )

    serving = graphene.Field(
        ServingNode,
        description = "Created serving."
    )

    errors = graphene.List(
        ErrorType,
        description = 'List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a serving."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # user = info.context.user
        # kwargs['input']['user'] = user
        form = ServingForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateServingMutation(
                errors = get_errors(form.errors)
            )
        serving = form.save()
        
        return CreateServingMutation(
            serving=serving
        )

class DeleteServingMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True,description="id to delete a serving")
    id=graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        redis_instance = redis.StrictRedis(host='localhost',
                                           port=6379, db=0)
        redis_instance.delete(str(id))

        serving = Serving.objects.get(gid=id)
        serving.delete()

        return DeleteServingMutation(
            id=id
        )


class UpdateServingMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="id to update a serving")
        input = ServingInput(
            required = True,
            description = "Fields required to create a serving."
        )

    serving = graphene.Field(
        ServingNode,
        description = "Updated serving."
    )

    errors = graphene.List(
        ErrorType,
        description = 'List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Updates a serving."

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        serving=Serving.objects.get(gid=id)
        form = ServingForm(data=kwargs['input'], instance=serving)

        if not form.is_valid():
            return UpdateServingMutation(
                errors = get_errors(form.errors)
            )
        serving = form.save()

        return UpdateServingMutation(
            serving=serving
        )



class SetCalledMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True,description="id to delete an order")
        called = graphene.Boolean(required=True)
    id = graphene.ID()
    called = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id,called):
        redis_instance = redis.StrictRedis(host='localhost',
                                           port=6379, db=0)

        if called:
            redis_instance.set(str(id), str(called))
        else:
            redis_instance.delete(str(id))

        return SetCalledMutation(
            id=id,
            called=called
        )


class Mutation(graphene.ObjectType):
    create_serving = CreateServingMutation.Field()
    delete_serving=DeleteServingMutation.Field()
    update_serving=UpdateServingMutation.Field()
    set_called=SetCalledMutation.Field()
