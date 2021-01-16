import graphene
from rx import Observable

from restaurant_entities.models.order import Order, Serving
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.order import (
    OrderList,
    OrderNode, OrderInput
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.order import OrderForm
from graphql.error import GraphQLError

import random


class Query(graphene.ObjectType):
    orders = graphene.Field(
        OrderList)

    order = graphene.Field(OrderNode, id=graphene.ID(required=True))

    def resolve_order(self, info, id):
        return Order.objects.get(gid=id)

    def resolve_orders(self, info, **kwargs):
        qs = Order.objects.all()
        return OrderList(qs)


class CreateOrderFrontendMutation(graphene.Mutation):
    class Arguments:
        serving_code = graphene.String(required=True, description="Serving code")

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
    def mutate(cls, root, info, serving_code, **kwargs):
        colors = ["#4C2C69", "#42253B", "#747572", "#E98A15", "#36393B", "#9F4A54","#0E1C36","#048A81","#00ABE7","#4CB5AE"]
       
        serving = Serving.objects.get(code=serving_code)
        
        # Return an error message if the table is full (no more colors available)
        if Order.objects.filter(serving=serving).count() >= len(colors):
            return CreateOrderFrontendMutation(
                errors=[ErrorType(message="Table is full.")] # TODO: Fix error message
            )

        random_color = random.choice(colors)
        while Order.objects.filter(serving=serving, color=random_color).exists():
            random_color = random.choice(colors)

        order = Order(serving=serving, color=random_color, note='', locked=False)
        order.save()

        return CreateOrderFrontendMutation(
            order=order
        )


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



class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()
    create_order_frontend = CreateOrderFrontendMutation.Field() 
    delete_order = DeleteOrderMutation.Field()
    update_order = UpdateOrderMutation.Field()