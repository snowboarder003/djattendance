from django.contrib import admin

from syllabus.models import Syllabus, Session, Assignment

admin.site.register(Syllabus)
admin.site.register(Session)
admin.site.register(Assignment)
