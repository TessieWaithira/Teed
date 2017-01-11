from django.test import TestCase
from howdy.models import Person



# Create your tests here.

class HowdyTest(TestCase):

	def test_str(self):

		people = Person(first_name='John', last_name='Smith')

		self.assertEquals(
			str(contact),
			'John Smith',
			) 