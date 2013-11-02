from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import Absentee, Roster, Entry

class EntryAdmin(admin.ModelAdmin):
	def house(obj):
		return obj.absentee.house

	def term(obj):
		return obj.absentee.term

	list_display = ('roster', 'absentee', 'reason', 'comments', house,)

admin.site.register(Absentee)
admin.site.register(Roster)
admin.site.register(Entry, EntryAdmin)