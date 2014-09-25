from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse,reverse_lazy
from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic import ListView
from .models import Badge
from accounts.models import User
from terms.models import Term
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BadgeForm, BadgeUpdateForm, BadgePrintForm
from .printtopdf import render_to_pdf
import xhtml2pdf.pisa as pisa

def index(request):
    return render_to_response('badges/badge_list.html')

def batch(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.term_created = Term.current_term()
        b.original = request.FILES['file']
        b.avatar = request.FILES['file']
        b.save()
        
        # grab the trainee name. filename in form of:
        # /path/to/Ellis_Armad.jpg or /path/to/Ellis_Armad_1.jpg
        name = b.original.name.split('/')[-1].split('.')[0].split('_')

        try:
            user = User.objects.get(Q(is_active=True), 
                                Q(firstname__exact=name[0]), 
                                Q(lastname__exact=name[1]))
        except User.DoesNotExist:
            print "Error User does not exist"

        if user:
            user.trainee.badge = b
            user.save()
            user.trainee.save()

    return render_to_response('badges/batch.html', context_instance=RequestContext(request))

def badgeprintout(request):
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = BadgePrintForm(request.POST)
    """
    return render_to_response('badges/print.html', Badge.objects.filter(term_created__exact=Term.current_term()))

def makepdf(request):
    return render_to_pdf(
            'print.html',
            {
                'pagesize':'A4',
            }
        )

class BadgePrintFrontView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/print.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFrontView, self).get_context_data(**kwargs)
        return context

class BadgePrintBackView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printback.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintBackView, self).get_context_data(**kwargs)
        return context

class BadgePrintGeneralBackView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printgeneralback.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintGeneralBackView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgePrintFacebookView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printfacebook.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFacebookView, self).get_context_data(**kwargs)
        return context

class BadgePrintStaffView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printstaff.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintStaffView, self).get_context_data(**kwargs)
        return context

class BadgePrintShorttermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printshortterm.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintShorttermView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgeTermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/term.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeTermView, self).get_context_data(**kwargs)
        return context

class BadgeXBTermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/xbterm.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeXBTermView, self).get_context_data(**kwargs)
        return context

class BadgeStaffView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/staff.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeStaffView, self).get_context_data(**kwargs)
        return context

class BadgeListView(ListView):
    model = Badge
    queryset = Badge.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BadgeListView, self).get_context_data(**kwargs)
        return context

class BadgeCreateView(CreateView):
    form_class = BadgeForm
    model = Badge
    success_url='/badges/'

    def get_context_data(self, **kwargs):
        context = super(BadgeCreateView, self).get_context_data(**kwargs)
        return context

class BadgeUpdateView(UpdateView):
    model = Badge
    template_name = 'badges/badge_detail.html'
    form_class = BadgeUpdateForm
    success_url='/badges/'
    
    def get_context_data(self, **kwargs):
        context = super(BadgeUpdateView, self).get_context_data(**kwargs)
        return context

class BadgeDeleteView(DeleteView):
    model = Badge
    template_name = 'badges/badge_delete.html'
    success_url='/badges/'

class BadgePrintUsherView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printusher.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintUsherView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgePrintTempView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printtemp.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintTempView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(50)]
        return context

class BadgePrintVisitorView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printvisitor.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintVisitorView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(50)]
        return context

class BadgePrintOfficeView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printoffice.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintOfficeView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

def genpdf(request):
    '''
    pdf = pisa.CreatePDF("Hello <strong>World</strong>",file('mypdf.pdf', 'wb'))
    if not pdf.err:
        pisa.startViewer('mypdf.pdf')
    return render_to_response('badges/printfacebook.html', context_instance=RequestContext(request))
    '''
    return render_to_pdf(
            'badges/printfbpdf.html', {}
        )





