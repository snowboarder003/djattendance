"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from classes.models import Class


class ClassTests(TestCase):
    def setUp(self):
        c1=Class.objects.create(name='Experience of Christ as Life', code='ECAL',type='1YR')
        c2=Class.objects.create(name='God Ordained Way', code='GOW',type='MAIN')
        c3=Class.objects.create(name='New Jerusalem', code='NJ',type='2YR')
        c4=Class.objects.create(name='Character', code='CHAR',type='AFTN')

    def test_class_type_choices(self):
        """
        Tests that the choice types matches
        CLASS_TYPE = (
        ('MAIN', 'Main'),
        ('1YR', '1st Year'),
        ('2YR', '2nd Year'),
        ('AFTN', 'Afternoon'),
         )  
        """
        c1=Class.objects.get(code='ECAL')
        c2=Class.objects.get(code='GOW')
        c3=Class.objects.get(code='NJ')
        c4=Class.objects.get(code='CHAR')

        self.assertEqual(c1.type, "1YR")
        self.assertEqual(c2.type, "MAIN")
        self.assertEqual(c3.type, "2YR")
        self.assertEqual(c4.type, "AFTN")