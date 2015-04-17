from django.contrib import admin

from .models import Template, Chart, Seat, Partial

admin.site.register(Template)
admin.site.register(Chart)
admin.site.register(Seat)
admin.site.register(Partial)
