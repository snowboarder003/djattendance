from django.test import TestCase
from buglog.models import Bug

"""
Bug submission
1. User submits bug using bug reporting form.
2. An attempt to connect to the GitHub repo is made; if successful, submits an issue.
3. The bug details are saved in the DB, including whether the issue was created, and 
the issue ID.

Bug resolution
1. User resolves the GitHub issue.
2. User goes to the attendance server and marks bug as resolved.
3. Bug is updated and saved as "resolved".
"""

class BuglogTest(TestCase):

    def test_submit_bug(self):
    	# creates a new bug object
    	# verify that it was saved

	def test_github_connection(self):
    	# verify connection to github api for issue creation (check authentication)

    def test_sync_bug(self):
    	# sync an existing bug object to an issue in GitHub

    def test_resolve_bug(self):
    	# create a bug object, mark it as resolved and verify save