from django.contrib import admin
from terms.models import Term

class TermAdmin(admin.ModelAdmin):
    date_hierarchy = 'start'

admin.site.register(Term)
