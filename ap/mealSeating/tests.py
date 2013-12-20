"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import date

from django.test import TestCase

from accounts.models import User, Trainee
from mealSeating.models import Table
from mealSeating.autofixtures import TraineeAutoFixture, UserAutoFixture


def setup_trainees_autofixture():
    """
        This is a test case for using autofixtures in a test.
    """
    user_fixture, trainee_fixture = UserAutoFixture(User), \
        TraineeAutoFixture(Trainee)
    users, trainees = user_fixture.create(25), trainee_fixture.create(25)

def setup_southeast_tables():
    """
        Creates all the table's in the southeast cafeteria
    """
    tables = []
    tables.append(Table(name="SE-01", capacity=8, location="SE", genderType="B").save())
    tables.append(Table(name="SE-02", capacity=8, location="SE", genderType="B").save())
    tables.append(Table(name="SE-03", capacity=8, location="SE", genderType="B").save())
    tables.append(Table(name="SE-04", capacity=8, location="SE", genderType="B").save())

    return tables

def setup_west_tables():
    """
        Creates all the table's in the west cafeteria
    """
    tables = []
    tables.append(Table(name="W-01", capacity=8, location="W").save())
    tables.append(Table(name="W-02", capacity=8, location="W").save())
    tables.append(Table(name="W-03", capacity=8, location="W").save())
    tables.append(Table(name="W-04", capacity=8, location="W").save())
    tables.append(Table(name="W-05", capacity=8, location="W").save())

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
    """
        This test checks the tables are created according to the right locations.
    """
    def test_create_tables_for_location(self):
        setup_southeast_tables()
        setup_west_tables()
        self.assertEqual(4, Table.objects.filter(location="SE").count())
        self.assertEqual(5, Table.objects.filter(location="W").count())


class TestMarriedCoupleFilter(TestCase):
    '''
        This test will check that the filter on the married couples is applied when seating the trainees
    '''
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

class TestTableCapacity(TestCase):
    '''
        This test will test the seatTrainee() function in the Table module to
        ensure that trainees will not be added beyond the capacity of the table.
    '''
    def test_seatTrainee_cannot_add_beyond_capacity(self):
        setup_trainees_autofixture()
        setup_southeast_tables()

        table = Table.objects.filter(location="SE").all()[0]
        traineesToSeat = Trainee.objects.filter(married=False)
        
        for trainee in traineesToSeat:
            table.seatTrainee(trainee)

        self.assertEqual(table.capacity, table.seatedTrainees.count())

class TestTableOverflow(TestCase):
    '''
        This test will test that trainees being added to a group of tables, will be able to 
        overflow from the first table to the next
    '''
    def test_seatTrainee_overflow(self):
        setup_trainees_autofixture()
        setup_southeast_tables()

        traineesToSeat = Trainee.objects.filter(married=False).order_by('account__firstname')

        Table.seatBrothers(traineesToSeat)
        
        self.assertLess(0, Table.objects.all()[1].getSeatedTrainees().count())
