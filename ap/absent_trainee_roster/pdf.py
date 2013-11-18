from django.template import Context
from django.http import HttpResponse
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from cgi import escape

context_dic ={}

def render_to_pdf(template_src, context_dict):
		template = get_template(template_src)
		context = Context(context_dic)
		html = template.render(context)
		result = StringIO.StringIO()
		
		pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
		if not pdf.err:
			return HttpResponse(result.getvalue(), mimetype = 'application/pdf')
		return HttpResponse('We had some errors<pre>%s</pre>' %escape(html))