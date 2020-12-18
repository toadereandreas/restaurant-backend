from django.apps import AppConfig


class RestaurantEntitiesConfig(AppConfig):
    name = 'restaurant_entities'

    def ready(self):
        import restaurant_entities.signals
