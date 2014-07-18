from datetime import date

from django.test import TestCase

from accounts.models import User
from absent_trainee_roster.models import Roster, Absentee


class RosterViewTestCase(TestCase):
	fixtures = ['initial_data.json', 'absent_trainee_roster_testdata.json']

	def test_absent_trainee_form(self):
		url = '/absent_trainee_roster/absent_trainee_form/'
		user = User.objects.all()[0]

		self.client.login(username=user.email, password='asdf')

		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

		formset = response.context['formset']
		self.assertEqual(len(formset.forms), 1)
		self.assertTrue(Roster.objects.get(date=date.today())) # today's roster was created

		# check that absentee choices are housemates
		absentee_choices = formset.forms[0].fields['absentee'].choices.queryset
		housemates = Absentee.objects.all().filter(account__trainee__house=user.trainee.house)
		self.assertEqual(len(absentee_choices), len(housemates))
		for housemate in housemates:
			self.assertTrue(housemate in absentee_choices)
		for absentee in absentee_choices:
			self.assertTrue(absentee in housemates)
