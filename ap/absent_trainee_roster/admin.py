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

from models import Absentee, Roster, Entry

from pdf import render_to_pdf


class RosterAdmin(admin.ModelAdmin):
	generate_roster = 'absent_trainee_roster/generate_roster.html'
	
	def get_urls(self):
		urls = super(RosterAdmin, self).get_urls()
		my_urls =patterns('',
			(r'\d+/generate/$', self.admin_site.admin_view(self.myview)),
		)
		return my_urls +urls
	
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
	
	#using Pisa
	def myview(self, request):
		#Retrieve data or whatever you need
		return render_to_pdf(
			'absent_trainee_roster/generate_roster.html',
			{
				'pagsize': 'A4',
				#'mylist': results,
			}
		)


class EntryAdmin(admin.ModelAdmin):
	def house(obj):
		return obj.absentee.house

	def term(obj):
		return obj.absentee.term

	list_display = ('roster', 'absentee', 'reason', 'comments', house,)

admin.site.register(Absentee)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Entry, EntryAdmin)

