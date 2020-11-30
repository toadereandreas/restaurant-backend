from .base import RestaurantObjectType
import graphene
from restaurant_entities.models.order import OrderMenuItem, Serving
from restaurant_entities.models.menu import MenuItem


class OrderMenuItemNode(RestaurantObjectType):
    class Meta:
        model = OrderMenuItem
        fields = [
            'gid',
            'menu_item',
            'order',
            'quantity'
        ]

    id = graphene.ID()
    color = graphene.String()
    serving_id = graphene.ID()
    menu_item_id = graphene.ID()


    def resolve_id(self, info):
        return OrderMenuItem.get_pk(gid=self.gid)

    def resolve_color(self, info):
        return self.order.color

    def resolve_serving_id(self, info):
        return Serving.get_pk(gid=self.order.serving.gid)

    def resolve_menu_item_id(self, info):
        return MenuItem.get_pk(gid=self.menu_item.gid)


class OrderMenuItemList(graphene.ObjectType):
    data = graphene.List(OrderMenuItemNode)


class OrderMenuItemInput(graphene.InputObjectType):
    menu_item = graphene.String()
    order = graphene.String()
    quantity = graphene.Int()
