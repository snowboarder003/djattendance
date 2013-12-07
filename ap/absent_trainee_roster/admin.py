from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.template import RequestContext, Context
from django.conf.urls import patterns
from django.shortcuts import render_to_response

from reportlab.pdfgen import canvas
from django.http import HttpResponse

import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from cgi import escape

from datetime import date, timedelta

from models import Absentee, Roster, Entry, House

from pdf import render_to_pdf


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
			#(r'\d+/generate/$', self.admin_site.admin_view(self.myview)),
			(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d+)/generate/$', self.admin_site.admin_view(self.myview)),
			
		)
		return my_urls +urls
	
	#using Pisa
	def myview(self, request, year, month, day):
		#Retrieve data or whatever you need
		d=date(int(year),int(month),int(day))
		roster = Roster.objects.get(date=d)
		entries = roster.entry_set.all().order_by('-absentee')
		bro_unreported_houses = roster.unreported_houses.filter(gender='B')
		sis_unreported_houses = roster.unreported_houses.filter(gender='S')
		
		days = self.calculate_days(d)
		unreported_list = self.list_unreported_houses(d)
		return render_to_pdf(
			'absent_trainee_roster/generate_roster.html',
			{
				'pagsize': 'letter',
				'roster': roster,
				'entries': entries,
				'bro_unreported_houses': bro_unreported_houses,
				'sis_unreported_houses': sis_unreported_houses,
				'days': days,
				'unreported_list': unreported_list,
				
			}
		)

	#calculate how many days a trainee has been absent in the last 7 days
	def calculate_days(self,date):
		days = {}
		for i in range(7):
			try:
				roster = Roster.objects.get(date=date)
				for entry in roster.entry_set.all():
					if str(entry.absentee) in days:
						days[str(entry.absentee)] += 1
					else:
						days[str(entry.absentee)] = 1
			except:
				pass
			
			date = date - timedelta(days=1)
		return days
	
	#makes list of trainee houses that are unreported within the last 7 days
	def list_unreported_houses(self, date):
		list = []
		for i in range(7):
			try:
				roster = Roster.objects.get(date=date)
				for house in roster.unreported_houses.all():
					if house not in list:
						list.append(house)
			except:
				pass
			
			date = date - timedelta(days=1)
		return list
	
	#using Reportlab
	def roster_pdf(self, request):
		#Create the HttpResponse object with the appropriate PDF headers
		response = HttpResponse(mimetype='application/pdf')
		response['Content-Disposition'] = 'attachment; filename=roster.pdf'
	
		#Create the PDF object, using the response object as its "file."
		p =canvas.Canvas(response)
	
		#Draw things on the PDF. Here's where the PDF generation happens.
		p.drawString(100, 100, "Hello world.")
	
		#Close the PDF object
		p.showPage()
		p.save()
		return response	
	
	def generate(self, request):
		#roster = Roster.objects.get(date=date)
		
		return render_to_response(self.generate_roster, {
			#'date': roster.date,
			#'unreported_houses': roster.unreported_houses,
			'opts': self.model._meta,
			#'root_path': self.admin_site.root_path,
		}, context_instance=RequestContext(request))
	
	
admin.site.register(Absentee)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Entry, EntryAdmin)
