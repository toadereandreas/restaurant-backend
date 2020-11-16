from .base import RestaurantObjectType
import graphene
from restaurant_entities.models import Booking


class BookingNode(RestaurantObjectType):
    class Meta:
        model = Booking
        fields = [
            'gid',
            'date_time',
            'table',
            'number_of_persons',
            'phone_number'
        ]


class BookingList(graphene.ObjectType):
    data = graphene.List(BookingNode)


class BookingInput(graphene.InputObjectType):
    date_time = graphene.DateTime()
    table = graphene.String()
    number_of_persons = graphene.Int()
    phone_number = graphene.String()
