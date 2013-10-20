from django.contrib import admin

from .models import Portion

class PortionAdmin(admin.ModelAdmin):
    list_display = ('approved', 'title', 'submitted_by', 'timestamp')

admin.site.register(Portion, PortionAdmin)