from django.contrib import admin

from aputils.models import Country, City, Address, Vehicle

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Vehicle)