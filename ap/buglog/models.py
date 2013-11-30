from datetime import datetime
import requests, json
from requests.auth import HTTPDigestAuth

from django.db import models
from django.forms import ModelForm, Textarea, RadioSelect

from .models import User


""" buglog models.py

This module allows users to submit a bug report, attempts to automatically create an 
issue in GitHub, and displays the bug log and statuses.

"""

LOG_TYPES = (
		('Bug', 'Bug'),
		('Suggestion', 'Suggestion'),
		('Comment', 'Other'),
	)

PRIORITY_TYPES = (
		(1, 'Low priority'),
		(2, 'Medium priority'),
		(3, 'High priority'),
	)

ISSUES_URL = 'https://api.github.com/repos/attendanceproject/djattendance/issues'
ADMIN_USER = 'ysbecca' # TODO - create an admin user on the djattendance project
POST_HEADER = { 'Content-Type': 'application/json', 'Authorization': 'token 56398b834f0277f4e609ef2ca11d2fc1d4663e78' }

# For testing - personal access token for username ysbecca (with push pull access):
# 56398b834f0277f4e609ef2ca11d2fc1d4663e78

class Bug(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	priority = models.IntegerField(default=0, choices=PRIORITY_TYPES)
	open_date = models.DateTimeField(default=datetime.now(), auto_now_add=True)
	close_date = models.DateTimeField(auto_now=True)
	issue_id = models.CharField(max_length=100)
	log_type = models.CharField(max_length=20, choices=LOG_TYPES, default='B')
	
	# save a DB read and just save the necessary data as extra fields
	user_id = models.IntegerField(default=0)
	firstname = models.CharField(default='First', verbose_name=u'first name', max_length=30)
	lastname = models.CharField(default='Last', verbose_name=u'last name', max_length=30)
	is_staff = models.BooleanField(default=False)
	
	def __unicode__(self):
		return 'submitted: ' + self.open_date.strftime('%m/%d/%Y') + ' by ' + self.get_name() + ': ' + self.description

	def get_name(self):
		return self.firstname + ' ' + self.lastname

	@staticmethod
	def get_all_issues():
		""" Retrieves all issues from the Github repo. """
		# TODO: only get the OPEN issues
		try:
			r = requests.get(ISSUES_URL)
			if(r.status_code == 200):
				issues = json.loads(r.text)
				return issues
			else:
				print 'Problem retrieving issues.'
				return False
		except ConnectionError:
			print 'No connection.'
			return False

	def create_issue(self):
		data = {
			'title': self.title + ' submitted by ' + self.get_name(),
			'body': self.description,
			'assignee': ADMIN_USER,
			'labels': self.log_type,
			}
		try:
			r = requests.post(ISSUES_URL, data=json.dumps(data), headers=POST_HEADER)
			if(r.status_code == 200 or r.status_code == 201):
				content = json.loads(r.text)
				self.issue_id = content['number']
				self.description += ' || CREATED AT ' + content['url']
				self.save()
				print self
			else:
				print 'Problem creating issue.'
		except:
			print 'No connection. Bug saved without GitHub issue.'

class BugForm(ModelForm):
	class Meta:
		model = Bug
		fields = ['title', 'log_type', 'description', 'priority']
		widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 10}),
            'priority': RadioSelect(),
        }



