from django.test import TestCase, RequestFactory

from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        Menu.objects.create(
            title="IceCream",
            price=80,
            Inventory=100
        )
        Menu.objects.create(
            title="Pizza",
            price=70,
            Inventory=10
        )

    def test_getall(self):
        menu_items = Menu.objects.all()
        serialized_menu_items = MenuSerializer(menu_items, many=True)
        request = self.factory.get('restaurant/menu/')
        response  = MenuItemView.as_view()(request)
        self.assertEqual(response.data, serialized_menu_items.data)