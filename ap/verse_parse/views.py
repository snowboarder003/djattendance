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

from verse_parse import references
from verses import print_reference, get_verses


def handle_uploaded_file(f):
	data = pdf_to_text(f)
	# title, rest = tsplit(data)
	outline = references.extract(data.partition('Scripture Reading:')[2])
	for outline_pt in outline:
		indent = ' '*((outline_pt[0]-1)*4)
		print(indent + outline_pt[1])
		for ref in outline_pt[2]:
			if ref[1] is not None:
				ref_string = print_reference(ref)
				print(indent + ref_string)
				# verses = get_verses(ref)
				# for verse in verses.values():
				# 	print verse
	return outline


def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			data=handle_uploaded_file(request.FILES['file'])
			
			display_template = loader.get_template('verse_parse/display_file.html')
			context = Context({'data': data,})
			return HttpResponse(display_template.render(context))
			"""
			outline = {'outline': data}
			form= DisplayForm(outline)
			c = {'form': form}
			return render_to_response('verse_parse/display_file.html', c)
			"""
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