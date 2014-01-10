from django import forms
from django.contrib import admin

from houses.models import House, Room, Bunk, MattressType, BedFrameType
from aputils.models import Address

class HouseAdminForm(forms.ModelForm):
    address = forms.ModelChoiceField(queryset=Address.objects.order_by('address1'))

    class Meta:
        model = House


class HouseAdmin(admin.ModelAdmin):
    form = HouseAdminForm
    list_display = (
        'name',
        'address',
        'gender',
        'used',
    )
    ordering = ('used', 'gender', 'name', 'address',)
    search_fields = ['name']


admin.site.register(House, HouseAdmin)
admin.site.register(Room)
admin.site.register(Bunk)
admin.site.register(MattressType)
admin.site.register(BedFrameType)