from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Booking, Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(APITestCase):
    def setUp(self):
        Menu.objects.create(title='Pizza', price=Decimal('12.50'), inventory=10)
        Menu.objects.create(title='Pasta', price=Decimal('9.00'), inventory=8)

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        expected = MenuSerializer(Menu.objects.all(), many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_create_update_and_delete_item(self):
        create_response = self.client.post(
            '/api/menu-items/',
            {'title': 'Salad', 'price': '6.50', 'inventory': 5},
            format='json',
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        item_id = create_response.data['id']
        update_response = self.client.put(
            f'/api/menu-items/{item_id}/',
            {'title': 'Greek Salad', 'price': '7.00', 'inventory': 4},
            format='json',
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        delete_response = self.client.delete(f'/api/menu-items/{item_id}/')
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)


class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='guest', password='safe-test-password'
        )

    def test_booking_list_requires_authentication(self):
        response = self.client.get('/restaurant/booking/tables/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            '/restaurant/booking/tables/',
            {
                'name': 'Grace',
                'no_of_guests': 3,
                'booking_date': date(2026, 12, 2).isoformat(),
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)


class AuthenticationViewTest(APITestCase):
    def test_user_registration_and_token_login(self):
        registration = self.client.post(
            '/auth/users/',
            {
                'username': 'newuser',
                'password': 'safe-test-password',
                're_password': 'safe-test-password',
            },
            format='json',
        )
        self.assertEqual(registration.status_code, status.HTTP_201_CREATED)

        login = self.client.post(
            '/auth/token/login/',
            {'username': 'newuser', 'password': 'safe-test-password'},
            format='json',
        )
        self.assertEqual(login.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', login.data)
