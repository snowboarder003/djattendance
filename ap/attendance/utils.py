# attendance utils.py
from datetime import date, timedelta

from terms.models import Term

class Period(object):
    """ a collection of methods related to calculating attendance periods """

    DURATION = 2  # number of weeks per period

    def period_of_week(week):
        """ for a week number, starting from zero, return the period """
        return week/self.duration + 1

    def period_of_date(date):
        """ for a calendar date, return the period """
        week, day = self.term.reverse_date(date)  # returns a week and a day
        return self.period_of_week(week)

    def start(n):
        """ for a period number, return the start date """
        wk = self.duration * (n-1)  # week number for start of this period
        return self.term.start + timedelta(weeks=wk)

    def end(n):
        """ for a period number, return end date """
        wk = n * self.duration  # week number for start of next period
        return self.term.start + timedelta(weeks=wk, days=-1) # and subtract one day

    def start_end(n):
        return self.start(n), self.end(n)

    def __init__(self, term=Term.current_term())
        self.term = term  # which term these periods apply to
        self.duration = DURATION