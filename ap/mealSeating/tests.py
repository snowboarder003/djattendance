"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import date

from django.test import TestCase

from accounts.models import User
from accounts.models import Trainee
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


def setup_normalTrainee():
    """
        Creates normal trainee that can be added to the meal seating list
    """
    brother = User(email="normalBrother@gmail.com", username="normalBrother",
                   firstname="David", is_active=True)
    brother.save()
    Trainee(account=brother, type="R", married=False,
            date_begin=date.today()).save()


def setup_marriedCouple():
    """
        Creates married couple which will be utlized in the following tests to
        ensure they are not added to the meal seating list
    """
    brother = User(email="marriedBrother@gmail.com", username="marriedBrother",
                   firstname="bob", is_active=True)
    sister = User(email="marriedSister@gmail.com", username="marriedSister",
                  firstname="merry", is_active=True)
    brother.save()
    sister.save()
    traineeBro = Trainee(account=brother, type="R", married=True,
                         date_begin=date.today()).save()
    Trainee(account=sister, type="R", married=True, spouse=traineeBro,
            date_begin=date.today()).save()


class TestTableCreation(TestCase):

    def test_create_tables(self):
        tables = setup_southeast_tables()
        self.assertEqual(4, len(tables))


class TestMarriedCoupleFilter(TestCase):

    def test_create_seating_without_married_couples(self):
        setup_normalTrainee()
        setup_marriedCouple()
        setup_southeast_tables()

        traineesToSeat = Trainee.objects.filter(married=False)
        tablesAvailable = Table.objects.filter(location="SE")

        [tablesAvailable.all()[0].seatedTrainees.add(trainee)
            for trainee in traineesToSeat]

        self.assertEqual(1, tablesAvailable.all()[0].seatedTrainees.count())
        self.assertEqual("David", tablesAvailable.all()[0].seatedTrainees.all()[0].account.get_full_name())

    def test_create_seating_with_married_couples(self):
        setup_normalTrainee()
        setup_marriedCouple()
        setup_southeast_tables()

        traineesToSeat = Trainee.objects.filter(married=True)
        tablesAvailable = Table.objects.filter(location="SE")

        [tablesAvailable.all()[0].seatedTrainees.add(trainee)
            for trainee in traineesToSeat]

        self.assertEqual(2, traineesToSeat.count())
        self.assertEqual(2, tablesAvailable.all()[0].seatedTrainees.count())
