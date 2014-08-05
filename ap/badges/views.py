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
from .forms import BadgeForm, BadgeUpdateForm

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

class TermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/term.html']

    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())

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

