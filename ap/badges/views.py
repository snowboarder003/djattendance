from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse,reverse_lazy
from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic import ListView
from .models import Badge
from accounts.models import User, Trainee
from terms.models import Term
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .forms import BadgeForm, BadgeUpdateForm, BadgePrintForm
from .printtopdf import render_to_pdf
import xhtml2pdf.pisa as pisa
import datetime

class index(ListView):
    model = Badge
    template_name = "badge_list.html"

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
    return render_to_response('badges/print.html', Badge.objects.filter(term_created__exact=Term.current_term()))

def pictureRange(begin, end):
    if begin>end:
        return []

    pictureRangeArray = []
    for num in range(int(begin-end)/8):
        pictureRangeArray = pictureRangeArray.append(begin+num*8)

    return pictureRangeArray

class BadgePrintFrontView(ListView):

    model = Badge

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_template_names(self):
        return ['badges/print.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFrontView, self).get_context_data(**kwargs)

        if 'choice' in self.request.POST:
            context['object_list'] = Badge.objects.filter(id__in=self.request.POST.getlist('choice'))

        return context

class BadgePrintMassFrontView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/print.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintMassFrontView, self).get_context_data(**kwargs)
  
        numTrainees = Trainee.objects.filter().all().count()
        #Signifies the range of pictures to place on the right side
        context['need_bottom_rightside'] = pictureRange(6, numTrainees)
        #Signifies the range of pictures to place on the left side
        context['need_bottom_leftside'] = pictureRange(7, numTrainees)

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
        return ['badges/printfbpdf.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    # Praise the Lord!!!!!!!
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFacebookView, self).get_context_data(**kwargs)
        context['first_term_brothers'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2015, season='Spring'), gender__exact='M')
        context['first_term_sisters'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2015, season='Spring'), gender__exact='F')

        context['second_term_brothers'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2014, season='Fall'), gender__exact='M')
        context['second_term_sisters'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2014, season='Fall'), gender__exact='F')

        context['third_term_brothers'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2014, season='Spring'), gender__exact='M')
        context['third_term_sisters'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2014, season='Spring'), gender__exact='F')

        context['fourth_term_brothers'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2013, season='Fall'), gender__exact='M')
        context['fourth_term_sisters'] = Badge.objects.filter(term_created__exact=Term.objects.get(year=2013, season='Fall'), gender__exact='F')

        context['current_term'] = Term().current_term

        
        """context['first_term'] = Badge.objects.filter(trainee__sss="R").count()
        """
        
        # context['first_term_pages'] = context['first_term']/20
        # context['loop_range'] = range(1,context['first_term_pages']+1)
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
    return render_to_response('badges/print.html')






