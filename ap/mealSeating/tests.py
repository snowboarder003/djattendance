"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mealSeating.models import Table


def setup_southeast_tables():
    """
        Creates all the table's in the southeast cafeteria
    """
    tables = []
    tables.append(Table(name="SE-01", capacity=8, location="SE").save())
    tables.append(Table(name="SE-02", capacity=8, location="SE").save())
    tables.append(Table(name="SE-03", capacity=8, location="SE").save())
    tables.append(Table(name="SE-04", capacity=8, location="SE").save())

    return tables


class TestTableCreation(TestCase):

    def test_create_tables(self):
        tables = setup_southeast_tables()
        self.assertEqual(4, len(tables))
