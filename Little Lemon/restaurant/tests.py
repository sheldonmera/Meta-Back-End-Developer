from django.test import TestCase

import json
from datetime import datetime
from django.test import TestCase, Client
from .models import Booking
from .forms import BookingForm  
from django.urls import reverse

class ReservationsViewTest(TestCase):
    def test_reservations_view(self):
        client = Client()
        response = client.get(reverse('bookings.html'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

class BookViewTest(TestCase):
    def test_book_view(self):
        client = Client()
        response = client.get(reverse('book.html')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')
    
    def test_book_post(self):
        client = Client()
        response = client.post(reverse('book.html'), data={'first_name': 'John', 'reservation_date': '2023-08-15', 'reservation_slot': 'morning'})
        self.assertEqual(response.status_code, 200)  

class BookingsViewTest(TestCase):
    def test_bookings_post(self):
        client = Client()
        data = {
            'first_name': 'John',
            'reservation_date': '2023-08-15',
            'reservation_slot': 'morning',
        }
        response = client.post(reverse('bookings.html'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)  

    def test_bookings_get(self):
        client = Client()
        response = client.get(reverse('bookings.html'), {'date': '2023-08-15'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        


