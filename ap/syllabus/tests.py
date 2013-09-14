"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from classes.models import Class
from syllabus.models import Syllabus, Session
from books.models import Book


class ClassTests(TestCase):
    def setUp(self):
        """
        Tests:
            - syllabus:
                - class: name -> code
            - row (session):
                - self: assignment -> date
                - syllabus: assignment -> syllabus
                - class: assignment -> syllabus -> class
                - book: assignment -> book

        Setup:
            - c: class objects
            - s: syllabus objects
            - r: rows (session) objects
        """

        # Book objects
        b1 = Book.objects.create(name="Young People's Training", code="YPT", Author="Witness Lee")

        # The Class objects
        c1 = Class.objects.create(name='Full Ministry of Christ', code='FMOC', type='MAIN')
        c2 = Class.objects.create(name='God Ordained Way', code='GOW', type='MAIN')
        c3 = Class.objects.create(name='New Jerusalem', code='NJ', type='2YR')
        c4 = Class.objects.create(name='Character', code='CHAR', type='AFTN')

        # The Syllabus objects
        s1 = Syllabus.objects.create(classSyllabus=c1)
        s2 = Syllabus.objects.create(classSyllabus=c2)
        s3 = Syllabus.objects.create(classSyllabus=c3)
        s4 = Syllabus.objects.create(classSyllabus=c4)

        # The rows/Sessions for the Syllabus
        r1 = Session.objects.create(date="9-10-13", topic="Bringing the Infinite God Into the Finite Man",
                                    book=b1, assignment="pgs 252-263", exam=0, syllabus=s1)
    def test_syllabus_code(self):
        """
        Test that the syllabus objects match the code;
        """

        s1 = Class.objects.get(classSyllabus="Full Ministry of Christ")
        self.assertEqual(s1.code, "FMOC")

    def test_row_assignment(self):
        """
        Test that the rows match with their assignment
        """
        r1 = Class.objects.get(assignment="pgs 252-263")

        # check row with self
        self.assertEqual(r1.date, "9-10-13")

        # check row with the book
        self.assertEqual(b1.code, "YPT")

        # check row with the syllabus
        self.assertEqual(r1.syllabus.code, "FMOC")

        # check row with the class
        self.assertEqual(r1.syllabus.)
