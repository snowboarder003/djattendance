"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


from books.models import Collection, Publisher, Book

class BookTests(TestCase):
	def setUp(self):
		c=Collection.objects.create(name="Life Studies", code="LS")
		p=Publisher.objects.create(name="Living Stream Ministry", code="LSM")
		b1=Book.objects.create(isbn=1234567890, name="Life Study of Genesis volume 1", code="LSG1", collection=c, publisher=p)
		b2=Book.objects.create(isbn=1234567891, name="Life Study of Genesis volume 2", code="LSG2", chapters=25, publisher=p)

	def test_for_foreignkey_in_Book_objects(self):
		"""
		Tests that the fields are inserted correctly
		"""
		c=Collection.objects.get(code="LS")
		p=Publisher.objects.get(code="LSM")
		b1=Book.objects.get(code="LSG1")
		b2=Book.objects.get(code="LSG2")
		self.assertEqual(c.name, "Life Studies")
		self.assertEqual(p.name, "Living Stream Ministry")
		self.assertEqual(b1.collection.name, "Life Studies")
		self.assertIsNone(b2.collection)
		self.assertIsNone(b1.chapters)