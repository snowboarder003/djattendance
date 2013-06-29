"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.test import TestCase
from terms.models import Term


def create_term(name, code, start):
    """
    Creates a term with the given `name`, 'code', 'start' and will create
    the end of the term date by adding 20 weeks to the start date.
    """
    return Term.objects.create(name=name, code=code, start=start, end=start + datetime.timedelta(7*20-1))


class TermModelTest(TestCase):
    def test_term_creation(self):
        """
        Tests that term object created successfully by checking the variables.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        self.assertEqual("Fall 2012", term.name)
        self.assertEqual("Fa12", term.code)
        self.assertEqual(datetime.date(2012, 8, 13), term.start)
        self.assertEqual((datetime.date(2012, 8, 13)+datetime.timedelta(7*20-1)), term.end)


class TermMethodTest(TestCase):
    def test_getDate_with_first_date(self):
        """
        getDate() should return the first date of the start of the term.
        NOTE: first week for a term is week 0, the first day of the week is thus also 0.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        week_one_day_one = term.getDate(0, 0)
        self.assertEqual(term.start, week_one_day_one)

    def test_getDate_with_last_date(self):
        """
        getDate() should return the last date of the term.
        NOTE: last week of a term is week 19, and the last day of a given week is 6.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        week_twenty_day_seven = term.getDate(19, 6)
        self.assertEqual(term.end, week_twenty_day_seven)

    def test_getDate_with_fixed_end_date(self):
        """
        getDate() should return the last date of the term.
        NOTE: last week of a term is week 19, and the last day of a given week is 6.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        week_twenty_day_seven = term.getDate(19, 6)
        self.assertEqual(datetime.date(2012, 12, 30), week_twenty_day_seven)

    def test_getDate_with_middle_date(self):
        """
        getDate() should return the date for a week and day of a term.
        NOTE: last first and last week of a term are 0 and 19 respectively,
        and first and last day of a given week are 0 and 6 respectively.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        week_four_day_four = term.getDate(3, 3)
        self.assertEqual(datetime.date(2012, 9, 6), week_four_day_four)

    def test_reverseDate_with_first_date(self):
        """
        reverseDate() should return the tuple of the first week and day for the given date of the term.
        NOTE: week and day both begin at 0.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        first_week_first_day = term.reverseDate(term.start)
        self.assertEqual((0, 0), first_week_first_day)

    def test_reverseDate_with_last_date(self):
        """
        reverseDate() should return the tuple of the last week and day for the given date of the term.
        NOTE: the last week for the term and day of a week both end at 19 and 6 respectively.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        last_week_last_day = term.reverseDate(term.end)
        self.assertEqual((19, 6), last_week_last_day)

    def test_reverseDate_with_middle_date(self):
        """
        reverseDate() should return the tuple of the first week and day for the given date of the term.
        NOTE: week and day both begin at 0.
        """
        term = create_term(name="Fall 2012", code="Fa12", start=datetime.date(2012, 8, 13))
        #note under the condition that week starts at 0 and day also starts at 0.
        fourth_week_fourth_day = term.reverseDate(term.start)
        self.assertEqual((3, 3), fourth_week_fourth_day)
