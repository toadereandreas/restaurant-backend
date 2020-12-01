import graphene
from rx import Observable

from restaurant_entities.models.order import Order
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.order import (
    OrderList,
    OrderNode, OrderInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.order import OrderForm
from graphql.error import GraphQLError


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
        id=graphene.ID(required=True,description="id to delete an orde")
    id=graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        serving = Serving.objects.get(gid=id)
        serving.delete()

        return DeleteServingMutation(
            id=id
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
    delete_order=DeleteOrderMutation.Field()
    update_order=UpdateOrderMutation.Field()


class Subscription(graphene.ObjectType):
    orders = graphene.Field(OrderList)
    order_created = graphene.Field(OrderNode)

    def resolve_orders(root, info):
        return Observable.interval(3000).map(lambda i: orders)

    def resolve_order_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Order)
        ).map(lambda event: event.instance)
