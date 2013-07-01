from django.contrib import admin

from services.models import Category, Service, Period

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Period)
