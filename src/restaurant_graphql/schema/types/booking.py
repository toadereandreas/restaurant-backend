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

    id = graphene.ID()

    def resolve_id(self, info):
        return Booking.get_pk(gid=self.gid)

class BookingList(graphene.ObjectType):
    data = graphene.List(BookingNode)


class BookingInput(graphene.InputObjectType):
    date_time = graphene.DateTime()
    table = graphene.String()
    number_of_persons = graphene.Int()
    phone_number = graphene.String()
