from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.core.context_processors import csrf
from django.template import RequestContext, Context,loader

from verse_parse.forms import UploadFileForm, DisplayForm

#imports for pdfminer
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO
import re

from verse_parse import references_objects as references
# from verses_objects import print_reference, get_verses

# from django.template import Context
# from django.http import HttpResponse
# import cStringIO as StringIO
# import xhtml2pdf.pisa as pisa
# from django.template.loader import get_template
# from cgi import escape

# def render_to_pdf(template_src, context_dict):
# 	template = get_template(template_src)
# 	context = Context(context_dict)
# 	html = template.render(context)
# 	result = StringIO.StringIO()

# 	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), mimetype = 'application/pdf')
# 	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

# def generate_pdf(self, outline):
# 	return render_to_pdf(
# 		'verse_parse/verse_sheet.html',
# 		{
# 			'outline': outline,
# 		})


def handle_uploaded_file(f):
	'''
	Takes uploaded pdf file, returns outline of verse references.
	Gets verse text from references.
	Basically gets all needed data for HTML template.
	'''
	data = pdf_to_text(f)
	# title, rest = tsplit(data)
	outline = references.extract(data.partition('Scripture Reading:')[2])
	# for outline_pt in outline:
	# 	point = outline_pt[0]
	# 	indent = ' '*((point.level-1)*4)
	# 	print(indent + point.string)

	# 	for ref in outline_pt[1]:
	# 		if ref.chapter is not None:
	# 			print(indent + ' '*len(point.string) + ref.string)
	# 			verses = ref.get_verses()
	# 			if verses:
	# 				for verse in verses.values():
	# 					print(verse)
	return outline


def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			data=handle_uploaded_file(request.FILES['file'])
			
			display_template = loader.get_template('verse_parse/verse_sheet.html')
			context = Context({'outline': data,})
			return HttpResponse(display_template.render(context))
			
		else:
			#return HttpResponse("Form invalid")
			c = {'form': form}
			c.update(csrf(request))
	
			return render_to_response('verse_parse/upload.html', c)
	else:
		form = UploadFileForm()
	
	c = {'form': form}
	c.update(csrf(request))
	
	return render_to_response('verse_parse/upload.html', c)


def pdf_to_text(fname):
    
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    codec = 'utf-8'
    caching = True
    showpageno = True
    laparams = LAParams()
    
   
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = StringIO()
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
    #fp = file(fname, 'rb')
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fname, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)
    #fp.close()
    device.close()
    #outfp.close()
    return outfp.getvalue()


# split outline by Roman Numerals and alphabets
def tsplit(text):
	list=re.split('\n(?P<bullet>[0-9A-Z-a-z][0-9A-Z]*\.)\s',text)
	title=list.pop(0)
	title=re.split('Scripture Reading:', title)
	dict={'title': title[0], 'Scripture Reading': title[1]}
	"""
	x=0
	for x in range(len(list)/2):
		dict[list[(x)]]=list[(x+1)]
		x=x+2
	"""
	return dict,list