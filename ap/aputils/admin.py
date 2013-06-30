from django import forms
from django.contrib import admin

from aputils.models import Country, City, Address, Vehicle

class AddressAdminForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.order_by('name'))

    class Meta:
        model = Address


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = (
        'address1', 
        'address2', 
        'city', 
        'zip_code', 
        'zip4', 
        'details'
    )
    ordering = ('address1', 'address2',)


class CityAdminForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.order_by('name'))

    class Meta:
        model = City


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = (
        'name',
        'region',
        'country'
    )
    ordering = ('country', 'region', 'name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code'
    )
    ordering = ('name', 'code',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'license_plate',
        'color',
        'make',
        'model'
    )
    ordering = ('make', 'model', 'color', 'license_plate',)


admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Vehicle, VehicleAdmin)