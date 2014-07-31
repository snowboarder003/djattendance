from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic import ListView
from .models import Badge
from accounts.models import User
from terms.models import Term
 
def index(request):

    return render_to_response('badges/index.html')

def batch(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.term_created = Term.current_term()
        b.original = request.FILES['file']
        b.save()

        # grab the trainee name. filename in form of:
        # /path/to/Ellis_Armad.jpg or /path/to/Ellis_Armad_1.jpg
        name = b.original.name.split('/')[-1].split('.')[0].split('_')

        user = User.objects.get(Q(is_active=True), 
                                Q(firstname__exact=name[1]), 
                                Q(lastname__exact=name[0]))

        user.trainee.badge = b
        user.save()

        return HttpResponseRedirect(reverse('badges:index'))
        

    return render_to_response('badges/batch.html', context_instance=RequestContext(request))

class TermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/term.html']

    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())