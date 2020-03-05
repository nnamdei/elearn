from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class TestUserRegistrationView(TestCase):

  def setUp(self):
    self.client = Client()

  def test_registration(self):
    url = reverse('student_registration')
    
    # test req method GET
    response = self.client.get(url)
    self.assertEqual(response.status, 200)

    # test req method POST with empty data
    response = self.client.post(url, {})
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': True,
      'errors': {
        'username': 'This field is required',
        'password': 'This field is required',
        'confirm': 'This field is required',
      }
    }
    self.assertEqual(exp_data, response.json())
    
    # test req method POST with invalid data
    req_data = {
      'username': 'user@test.com',
      'password': 'secret',
      'confirm': 'secret1',
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': True,
      'errors': {
        'confirm': 'Passwords mismatched'
      }
    }
    self.assertEqual(exp_data, response.json())

    # test req method POST with valid data
    req_data = {
      'username': 'user@test.com',
      'password': 'secret',
      'confirm': 'secret',
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': False,
      'message': 'Success, Please login'
    }
    self.assertEqual(exp_data, response.json())
    self.assertEqual(User.objects.count(), 1)
