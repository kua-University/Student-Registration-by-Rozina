# django_srs/students/tests/test_views.py

import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestPaymentViews:

    def test_payment_view(self, client):
        """Test the payment view."""
        response = client.get(reverse('payment'))  
        assert response.status_code == 200
        assert 'amount' in response.context
        assert response.context['amount'] == 2100
        assert response.template_name[0] == 'payment/chapa.html'

    def test_next_view(self, client):
        """Test the next view."""
        response = client.get(reverse('next'))  
        assert response.status_code == 200
        assert response.template_name[0] == 'payment/next.html'
