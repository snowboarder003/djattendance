"""
Refer also to books/tests for unit-test example
"""

from books.models import Collection, Publisher, Book, Author
import unittest

def set_up_data():
        # model1: Class without term, all types tested
        c1=Class(name='Experience of Christ as Life', code='ECAL',type='1YR')
        c2=Class(name='God Ordained Way', code='GOW',type='MAIN')
        c3=Class(name='New Jerusalem', code='NJ',type='2YR')
        c4=Class(name='Character', code='CHAR',type='AFTN')

class ClassesTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_models(self):
        data_dicts = set_up_data()
        self.assertTrue(Collection(data_dicts['c']))
        self.assertTrue(Publisher(data_dicts['p']))
        self.assertTrue(Author(data_dicts['a']))
        self.assertTrue(Book(data_dicts['b1']))
        self.assertTrue(Book(data_dicts['b2']))

    def test_class_type_choices(self):
        
        c1=Class.objects.get(code='ECAL')
        c2=Class.objects.get(code='GOW')
        c3=Class.objects.get(code='NJ')
        c4=Class.objects.get(code='CHAR')

        self.assertEqual(c1.type, "1YR")
        self.assertEqual(c2.type, "MAIN")
        self.assertEqual(c3.type, "2YR")
        self.assertEqual(c4.type, "AFTN")
