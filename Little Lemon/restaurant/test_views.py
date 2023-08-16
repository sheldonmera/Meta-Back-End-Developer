from django.test import TestCase, RequestFactory
from .models import Booking, Category, Menu
from .views import reservations, book, menu, display_menu_item
from .forms import BookingForm  

class ReservationsViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.booking = Booking.objects.create(first_name="John", reservation_date=date(2023, 8, 16), reservation_slot=5)

    def test_reservations_view(self):
        request = self.factory.get('/reservations/')
        response = reservations(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')  # Check if John's booking is present in the response


class BookViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.form_data = {'first_name': 'Jane', 'reservation_date': date(2023, 8, 17), 'reservation_slot': 10}

    def test_book_view_GET(self):
        request = self.factory.get('/book/')
        response = book(request)
        self.assertEqual(response.status_code, 200)

    def test_book_view_POST_valid_form(self):
        request = self.factory.post('/book/', data=self.form_data)
        response = book(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Booking.objects.filter(first_name='Jane').exists())


class MenuViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(slug='appetizers', title='Appetizers')
        self.menu_item = Menu.objects.create(title='Spring Rolls', price=9.99, category=self.category)

    def test_menu_view(self):
        request = self.factory.get('/menu/')
        response = menu(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spring Rolls')  # Check if Spring Rolls is present in the response



class DisplayMenuItemViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(slug='appetizers', title='Appetizers')
        self.menu_item = Menu.objects.create(title='Spring Rolls', price=9.99, category=self.category)

    def test_display_menu_item_view_with_pk(self):
        request = self.factory.get('/menu/item/1/')  # Assuming the primary key of the menu item is 1
        response = display_menu_item(request, pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spring Rolls')

    def test_display_menu_item_view_without_pk(self):
        request = self.factory.get('/menu/item/')
        response = display_menu_item(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['menu_item'], "")

