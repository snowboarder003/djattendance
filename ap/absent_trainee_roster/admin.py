from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import Absentee, Roster, Entry

class EntryAdmin(admin.ModelAdmin):
	def house(obj):
		return obj.absentee.house

	def term(obj):
		return obj.absentee.term

	list_display = ('roster', 'absentee', 'reason', 'comments', house,)


class EntryInline(admin.TabularInline):
	model = Entry
	fk_name = 'roster'
	verbose_name_plural = 'entries'
	extra = 1


class RosterAdmin(admin.ModelAdmin):
	inlines = [
		EntryInline,
	]

admin.site.register(Absentee)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Entry, EntryAdmin)