from django.test import TestCase
from .models import Booking, Menu
from decimal import Decimal

# Create your tests here.
class MenuTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.menuItem = Menu.objects.create(
            title="Pizza",
            price=Decimal('9.99'),
            inventory=100
        )

    def test_menu_item_creation(self):
        # If at any point you write 9.99, it will be interpreted as a float,
        # which can lead to precision issues. Use Decimal interpreted from
        # a string to get the exact value.
        self.assertEqual(self.menuItem.price, Decimal('9.99'))
        self.assertEqual(self.menuItem.inventory, 100)
        # self.menuItem is a Menu instance and must be wrapped in str().
        self.assertEqual(str(self.menuItem), 'Pizza - $9.99')