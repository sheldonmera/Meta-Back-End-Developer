from django.test import TestCase
from datetime import date
from .models import Booking, Category, Menu

#Models testCase

class BookingModelTestCase(TestCase):

    def setUp(self):
        Booking.objects.create(first_name="John", reservation_date=date(2023, 8, 16), reservation_slot=5)

    def test_booking_str(self):
        booking = Booking.objects.get(first_name="John")
        self.assertEqual(str(booking), "John")

    

class CategoryModelTestCase(TestCase):

    def setUp(self):
        Category.objects.create(slug="category-1", title="Appetizers")

    def test_category_str(self):
        category = Category.objects.get(slug="category-1")
        self.assertEqual(str(category), "Appetizers")

    

class MenuModelTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(slug="category-1", title="Appetizers")
        Menu.objects.create(title="Spring Rolls", price=9.99, category=category)

    def test_menu_str(self):
        menu = Menu.objects.get(title="Spring Rolls")
        self.assertEqual(str(menu), "Spring Rolls")

    




