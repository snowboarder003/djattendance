from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import Absentee, Roster

admin.site.register(Absentee)
admin.site.register(Roster)