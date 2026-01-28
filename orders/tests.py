from django.test import TestCase
from django.urls import reverse

class OrderViewTest(TestCase):
    def test_orders_status_code(self):
        url = reverse('order_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
