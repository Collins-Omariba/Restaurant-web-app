from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, Inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")