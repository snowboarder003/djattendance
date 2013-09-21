"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from classes.models import Class
from terms.models import Term
from syllabus.models import Syllabus, Session
from books.models import Book, Collection, Publisher, Author


class SyllabusTests(TestCase):
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
        k1 = Collection.objects.create(name="Collected Works of Witness Lee", code="CWWL")
        p1 = Publisher.objects.create(name="Living Stream Ministry", code="LSM")
        a1 = Author.objects.create(first_name="Witness", last_name="Lee", code="WL")

        b1 = Book.objects.create(isbn="27808707", name="Young People's Training", code="YPT",
                                 chapters=12, collection=k1, publisher=p1)

        # The Class objects
        t1 = Term.objects.create(name="Fall 2013", code="F13", season="Fall",
                                 start="2013-08-13", end="2013-12-28")

        c1 = Class.objects.create(name='Full Ministry of Christ', code='FMOC',
                                  type='MAIN', term=t1)
        c2 = Class.objects.create(name='God Ordained Way', code='GOW', type='MAIN', term=t1)
        c3 = Class.objects.create(name='New Jerusalem', code='NJ', type='2YR', term=t1)
        c4 = Class.objects.create(name='Character', code='CHAR', type='AFTN', term=t1)

        # The Syllabus objects
        s1 = Syllabus.objects.create(classSyllabus=c1)
        # Identify syllabus by ID #
        s1.type_id = 2

        s2 = Syllabus.objects.create(classSyllabus=c2)
        s3 = Syllabus.objects.create(classSyllabus=c3)
        s4 = Syllabus.objects.create(classSyllabus=c4)

        # The rows/Sessions for the Syllabus
        """ Q: How to change assignment from char field i.e.: ("") to Post()? """
        r1 = Session.objects.create(date="2013-09-10",
                                    topic="Bringing the Infinite God Into the Finite Man",
                                    book=b1, assignment=['BPEL, ch1', '1 John 5:12; Col 3:4; John 11:25; 14:6; 10:10'],
                                    exam=False, syllabus=s1)
        #r1.assignment = x1

    def test_syllabus_code(self):
        """
        Test that the syllabus objects match the code;
        """

        s1 = Syllabus.objects.get(session=2)
        self.assertEqual(s1.classSyllabus.code, "FMOC")

    def test_row_assignment(self):
        """
        Test that the rows match with their assignment
        """
        r1 = Session.objects.get(date="2013-09-10")

        self.assertEqual(r1.assignment[0], 'BPEL, ch1')
        self.assertEqual(r1.assignment[1], '1 John 5:12; Col 3:4; John 11:25; 14:6; 10:10')

        # self assert
        """ TO DO: Fix __UNICODE__ SELF TEST """
        self.assertEqual(r1, "Class: Full Ministry of Christ; Term: Fall 2013; Date: 2013-09-10; Topic: Bringing the Infinite God Into the Finite Man")

        # check row with self
        self.assertEqual(r1.topic, "Bringing the Infinite God Into the Finite Man")

        # check row with the book
        self.assertEqual(r1.book.code, "YPT")

        # check row with the syllabus
        self.assertEqual(r1.syllabus.classSyllabus.code, "FMOC")

        # check row with the class
