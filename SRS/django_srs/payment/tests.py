from django.test import TestCase, Client
from django.urls import reverse

#integration testing
"""test for urls.py"""
class URLTestCase(TestCase):
    def test_payment_url(self):
        url = reverse('payment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_next_url(self):
        url = reverse('next')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
     
#integration testing      
"""test for views.py"""    
class NextViewTest(TestCase):
    def test_next_view_returns_200(self):
        response = self.client.get(reverse('next'))
        self.assertEqual(response.status_code, 200)
        
    def test_next_view_renders_correct_template(self):
        response = self.client.get(reverse('next'))
        self.assertEqual(response.templates[0].name, 'payment/next.html')

class PaymentViewTest(TestCase):
    def test_payment_view_renders_correct_template(self):
        response = self.client.get(reverse('payment'))
        self.assertEqual(response.templates[0].name, 'payment/chapa.html')

    def test_payment_view_returns_200(self):
        response = self.client.get(reverse('payment'))
        self.assertEqual(response.status_code, 200)

    def test_payment_view_passes_correct_context(self):
        response = self.client.get(reverse('payment'))
        self.assertIn('amount', response.context)
        self.assertEqual(response.context['amount'], 2100)