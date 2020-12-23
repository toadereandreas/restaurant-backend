import graphene
from rx import Observable

from restaurant_entities.models.order import Order
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.order import (
    OrderList,
    OrderNode, OrderInput, SetLockedInput
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.order import OrderForm
from graphql.error import GraphQLError

import redis


class Query(graphene.ObjectType):
    orders = graphene.Field(
        OrderList) #,
        #id=graphene.ID(),
    #)
    order = graphene.Field(OrderNode, id=graphene.ID(required=True))

    def resolve_order(self, info, id):
        return Order.objects.get(gid=id)

    def resolve_orders(self, info, **kwargs):
        qs = Order.objects.all()
        return OrderList(qs)


class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        input = OrderInput(
            required = True,
            description = "Fields required to create an order."
        )

    order = graphene.Field(
        OrderNode,
        description = "Created order."
    )

    errors = graphene.List(
        ErrorType,
        description = 'List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates an order."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # user = info.context.user
        # kwargs['input']['user'] = user
        # kwargs['input']['serving'] = "1a857052-5628-4bd9-a378-45fbf960ecde"
        form = OrderForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateOrderMutation(
                errors = get_errors(form.errors)
            )
        order = form.save()
        return CreateOrderMutation(
            order=order
        )



class DeleteOrderMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True,description="id to delete an order")
    id=graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        order = Order.objects.get(gid=id)
        order.delete()

        return DeleteOrderMutation(
            id=id
        )


class UpdateOrderMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="id to update an order")
        input = OrderInput(
            required = True,
            description = "Fields required to create an order."
        )

    order = graphene.Field(
        OrderNode,
        description = "Updated order."
    )

    errors = graphene.List(
        ErrorType,
        description = 'List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Updates an order."

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        order=Order.objects.get(gid=id)
        form = OrderForm(data=kwargs['input'], instance=order)

        if not form.is_valid():
            return UpdateOrderMutation(
                errors = get_errors(form.errors)
            )
        order = form.save()

        return UpdateOrderMutation(
            order=order
        )


class SetFieldMutation(graphene.Mutation):
    # class Arguments:
    #     id = graphene.ID(required=True, description="id to update an order")
    #     input = SetLockedInput(
    #         required = True,
    #         description = "Fields required to set locked field for an order."
    #     )

    # order = graphene.Field(
    #     OrderNode,
    #     description = "Updated locked."
    # )

    # errors = graphene.List(
    #     ErrorType,
    #     description = 'List of errors that occurred executing the mutation.'
    # )
    #
    # class Meta:
    #     description = "Updates an order."

    # @classmethod
    # def mutate(cls, root, info, id):
    #     order = Order.objects.get(gid=id)
    #     order.delete()
    #
    #     return SetFieldMutation(
    #         id=id
    #     )

    # redis_instance = redis.StrictRedis(host='localhost',
    #                                    port=6379, db=0)

    # def manage_item(self,request, key, new_value=0):
    #     if request == 'GET':
    #         return redis_instance.get(key)
    #
    #     elif request == 'PUT':
    #         new_value = request_data['new_value']
    #         value = redis_instance.get('key')
    #         if value:
    #             redis_instance.set(key, new_value)
    #         return value


    class Arguments:
        id=graphene.ID(required=True,description="id to delete an order")
        # input = SetLockedInput(
        #     required = True,
        #     description = "Fields required to set locked field for an order."
        # )
        locked = graphene.Boolean(required=True)
    id=graphene.ID()
    locked = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id,locked):
        # order = Order.objects.get(gid=id)
        # order.delete()
        redis_instance = redis.StrictRedis(host='localhost',
                                           port=6379, db=0)

        redis_instance.set(str(id), str(locked))

        return DeleteOrderMutation(
            id=id
        )



    
class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()
    delete_order=DeleteOrderMutation.Field()
    update_order=UpdateOrderMutation.Field()
    set_field=SetFieldMutation.Field()
