import graphene

from restaurant_entities.models import Booking
from restaurant_graphql.schema.types.base import ErrorType
from restaurant_graphql.schema.types.booking import (
    BookingList,
    BookingNode, BookingInput,
)

from restaurant_graphql.schema.helpers import get_errors
from restaurant_graphql.forms.booking import BookingForm
from graphql.error import GraphQLError


class Query(graphene.ObjectType):
    bookings = graphene.Field(BookingList)
    booking = graphene.Field(BookingNode, id=graphene.ID(required=True))

    def resolve_booking(self, info, id):
        return Booking.objects.get(gid=id)

    def resolve_bookings(self, info, **kwargs):
        qs = Booking.objects.all()
        return BookingList(qs)


class CreateBookingMutation(graphene.Mutation):
    class Arguments:
        input = BookingInput(
            required=True,
            description="Fields required to create a booking."
        )

    booking = graphene.Field(
        BookingNode,
        description='Created booking.'
    )

    errors = graphene.List(
        ErrorType,
        description='List of errors that occurred executing the mutation.'
    )

    class Meta:
        description = "Creates a booking."

    @classmethod
    def mutate(cls, root, info, **kwargs):
        form = BookingForm(data=kwargs['input'])

        if not form.is_valid():
            return CreateBookingMutation(
                errors=get_errors(form.errors)
            )
        booking = form.save()

        return CreateBookingMutation(
            booking=booking
        )


class Mutation(graphene.ObjectType):
    create_booking = CreateBookingMutation.Field()
