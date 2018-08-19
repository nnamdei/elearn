from django.test import TestCase
from .models import User
from django.views.generic import FormView
from .forms import RegistrationForm
from django.http import JsonResponse

#test for models
class UserTestCase(TestCase):
	def setUp(self):
		self.author = User.objects.create(
			username='author@test.com',
			email = 'author@test.com',
			user_type = User.AUTHOR)
		self.publisher = User.objects.create(
			username='publisher@test.com',
			email='publisher@test.com',
			user_type=User.AUTHOR)

		def test_get_authors(self):
			self.assertEqual(User.get_authors(),1)

		def test_can_write_books(self):
			self.assertTrue(self.author.can_write_books())
			self.assertFalse(self.publisher.can_write_books())


class UserRegistrationView(FormView):
	form_class = RegistrationForm

	def form_valid(self,form):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		User.objects.create_user(username,password=password)
		res_data={
		'error':False,
		'message': 'Success, Please login'
		}
		return JsonResponse(res_data)

	def form_invalid(self,form):
		res_data = {
		'error':True,
		'errors': form.errors
		}
		return JsonResponse(res_data)
