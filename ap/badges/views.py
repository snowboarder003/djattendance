from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
 
from .forms import UploadBadgeForm
from .models import Badge
 
def home(request):

    return render_to_response('badge/index.html')

def upload(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.original = request.FILES['file']
        b.save()

        return HttpResponseRedirect(reverse('badges:home'))
        

    return render_to_response('badges/index.html', context_instance=RequestContext(request))
