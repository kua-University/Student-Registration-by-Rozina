from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SystemTestCase(TestCase):


    def test_login_and_render_home_page(self):
        # Log in the user
        login_response = self.client.post(reverse('login'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(login_response.status_code, 200)  # Assuming 200 OK

        # Check if the home page is rendered after login
        home_response = self.client.get(reverse('home'))  
        self.assertEqual(home_response.status_code, 200)  
        self.assertContains(home_response, "Welcome")  
        
    def setUp(self):
        # Create a user for testing registration and login
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        self.user = User.objects.create_user(**self.user_data)
 
    def test_user_registration_valid(self):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, 201)  # Assuming 201 Created
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_registration_invalid(self):
        # Test with missing username
        invalid_data = {
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        response = self.client.post(reverse('register'), invalid_data)
        self.assertEqual(response.status_code, 400)  # Assuming 400 Bad Request
