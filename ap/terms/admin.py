from django.contrib import admin
from terms.models import Term

##class TermAdmin(admin.ModelAdmin):
##    fieldsets = [
##        (None, {'fields': ['name']}),
##    ]
    
        
##    fieldsets = [
##        (None, {'fields': ['name']}),
##        ('Code', {'fields': ['code']}),
##        ('Start', {'fields': ['start']}),
##        ('End', {'fields': ['end']}),
##    ]
##    date_hierarchy = 'start'

admin.site.register(Term)
