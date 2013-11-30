from django.contrib import admin
from django.db import models
from django.template import RequestContext
from django.conf.urls.defaults import patterns
from django.shortcuts import render_to_response

from models import Absentee, Roster, Entry, House


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
	generate_roster = 'absent_trainee_roster/generate_roster.html'
	
	inlines = [
		EntryInline,
	]

	readonly_fields = ('unreported_houses',)

	# when roster is created, add all houses as unreported.
	# --this is also done in RosterManager.create_roster(), but  
	# admin doesn't call this function to create objects.
	def save_related(self, request, form, formsets, change):
		if change == False:
			roster = Roster.objects.get(date=request.REQUEST['date'])
			for house in House.objects.all():
				roster.unreported_houses.add(house)
			roster.save()
		return True


	def get_urls(self):
		urls = super(RosterAdmin, self).get_urls()
		my_urls =patterns('',
			(r'\d+/generate/$', self.admin_site.admin_view(self.hello_pdf)),
		)
		return my_urls +urls
	
	def generate(self, request):
		#roster = Roster.objects.get(date=date)
		
		return render_to_response(self.generate_roster, {
			#'date': roster.date,
			#'unreported_houses': roster.unreported_houses,
			'opts': self.model._meta,
			#'root_path': self.admin_site.root_path,
		}, context_instance=RequestContext(request))
	
	def hello_pdf(self, request):
		#Create the HttpResponse object with the appropriate PDF headers
		response = HttpResponse(mimetype='application/pdf')
		response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	
		#Create the PDF object, using the response object as its "file."
		p =canvas.Canvas(response)
	
		#Draw things on the PDF. Here's where the PDF generation happens.
		p.drawString(100, 100, "Hello world.")
	
		#Close the PDF object
		p.showPage()
		p.save()
		return response	


admin.site.register(Absentee)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Entry, EntryAdmin)
