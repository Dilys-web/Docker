import unittest
from flask import Flask
from app import app  
from bs4 import BeautifulSoup

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.client = app.test_client()
        self.client.testing = True

    def test_home_route(self):
        # Test the home route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Flask App!', response.data)
        self.assertIn(b'Greet Me!', response.data)

    def test_greet_route(self):
        # Test the greet route with a sample name
        response = self.client.get('/greet/Alice')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Alice!', response.data)

    def test_about_route(self):
        # Test the about route
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About This App', response.data)
        self.assertIn(b'Go back to Home', response.data)

    def test_register_route_get(self):
        # Test the register route with GET
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)
        self.assertIn(b'Name:', response.data)

    def test_register_route_post(self):
        # Fetch the registration form to get the CSRF token
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        
        # Extract CSRF token from the form
        soup = BeautifulSoup(response.data, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

        # Send POST request with CSRF token
        response = self.client.post('/register', data={
            'name': 'John',
            'csrf_token': csrf_token
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful! Welcome, John!', response.data)

if __name__ == '__main__':
    unittest.main()

