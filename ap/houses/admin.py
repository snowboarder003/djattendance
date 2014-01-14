from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from accounts.models import Trainee

from houses.models import House, Room, Bunk, MattressType, BedFrameType
from aputils.models import Address

class HouseAdminForm(forms.ModelForm):
    address = forms.ModelChoiceField(queryset=Address.objects.order_by('address1'))

    class Meta:
        model = House


class RoomInline(admin.TabularInline):
    model = Room
    
    def admin_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.module_name),  args=[instance.pk] )
        return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url))

    readonly_fields = ('admin_link',)

class HouseAdmin(admin.ModelAdmin):
    form = HouseAdminForm
    list_display = (
        'name',
        'address',
        'gender',
        'used',
    )
    inlines = [ RoomInline ]
    ordering = ('used', 'gender', 'name', 'address',)
    search_fields = ['name']
    

class BunkInlineForm(forms.ModelForm):
    trainee = forms.ModelChoiceField(queryset=Trainee.objects.filter(active=True).order_by('account__lastname','account__firstname'))
    
    class Meta:
        model = Bunk

class BunkInline(admin.StackedInline):
    model = Bunk
    form = BunkInlineForm 
    readonly_fields = ('link',)
    
class RoomAdmin(admin.ModelAdmin):
    inlines = [ BunkInline ]


admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Bunk)
admin.site.register(MattressType)
admin.site.register(BedFrameType)