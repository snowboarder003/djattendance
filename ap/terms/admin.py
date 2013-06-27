from django.contrib import admin
from terms.models import Term
from terms.forms import NewTermForm

class TermAdmin(admin.ModelAdmin):
    ordering = ['-start']
    form = NewTermForm

admin.site.register(Term, TermAdmin)
