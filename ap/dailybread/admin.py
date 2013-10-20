from django.contrib import admin

from .models import Portion

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)

class PortionAdmin(admin.ModelAdmin):
    list_display = ('approved', 'title', 'submitted_by', 'timestamp')
    actions = [approve]

admin.site.register(Portion, PortionAdmin)