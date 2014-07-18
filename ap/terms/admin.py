from django.contrib import admin
from terms.models import Term
from terms.forms import NewTermForm

class TermAdmin(admin.ModelAdmin):
    ordering = ['start']

admin.site.register(Term, TermAdmin)
