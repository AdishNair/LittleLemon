from datetime import date
from decimal import Decimal

from django.test import TestCase

from restaurant.models import Booking, Menu


class MenuModelTest(TestCase):
    def test_string_representation(self):
        item = Menu.objects.create(
            title='IceCream', price=Decimal('80.00'), inventory=100
        )

        self.assertEqual(str(item), 'IceCream : 80.00')


class BookingModelTest(TestCase):
    def test_string_representation(self):
        booking = Booking.objects.create(
            name='Ada', no_of_guests=2, booking_date=date(2026, 12, 1)
        )

        self.assertEqual(str(booking), 'Ada - 2026-12-01')
