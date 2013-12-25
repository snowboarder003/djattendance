from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.db.models import Q
 
from .forms import UploadBadgeForm
from .models import Badge

from accounts.models import User
 
def home(request):

    return render_to_response('badge/index.html')

def batch(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.original = request.FILES['file']
        b.save()

        # grab the trainee name
        last, first, ext = b.original.name.split('/')[-1].split('.')

        user = User.objects.get(Q(is_active=True), 
                                   Q(firstname__exact=first), 
                                   Q(lastname__exact=last))

        user.trainee


        return HttpResponseRedirect(reverse('badges:home'))
        

    return render_to_response('badges/index.html', context_instance=RequestContext(request))
