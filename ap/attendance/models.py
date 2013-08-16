from django.db import models

""" attendance models.py 
The attendance module takes care of data and logic related to tracking attendance.
It does not handle things such as schedules or leave slips. 

DATA MODELS:
	- Roll: an attendance record per trainee, per event. 
			for example, if 10 trainees are supposed to be at an event,
			then there will be 10 roll objects associated to that event,
			as well as each trainee.
	- Period: a set of attendance records, generally a 2-week period
"""

