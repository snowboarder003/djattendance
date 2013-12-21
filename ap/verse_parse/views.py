from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.core.context_processors import csrf
from django.template import RequestContext

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


def handle_uploaded_file(f):
	result = pdf_to_text(f)
			

def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('verse_parse/display_file.html')
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
    fp = file(fname, 'rb')
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)
    fp.close()
    device.close()
    #outfp.close()
    return outfp.getvalue()

def display_pdf(request, data):
	form = DisplayForm(initial=data)
	
	c = {'form': form}
	c.update(csrf(request))
	
	return render_to_response('verse_parse/display_file.html', c)
