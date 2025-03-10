from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu, Booking
from ..serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.menu2 = Menu.objects.create(title='Pizza', price=200, inventory=50)
        self.menu3 = Menu.objects.create(title='Burger', price=100, inventory=70)

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)