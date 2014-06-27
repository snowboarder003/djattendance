from django.contrib import admin
from schedules.models import *

admin.site.register(Event)
admin.site.register(EventGroup)
admin.site.register(Schedule)
admin.site.register(ScheduleTemplate)

