from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import Absentee

admin.site.register(Absentee)