from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.db.models import Q
 
from .forms import UploadBadgeForm
from .models import Badge

from accounts.models import User
 
def index(request):

    return render_to_response('badges/index.html')

def batch(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.original = request.FILES['file']
        b.save()

        # grab the trainee name
        name = b.original.name.split('/')[-1].split('.')[0].split('_')

        user = User.objects.get(Q(is_active=True), 
                                Q(firstname__exact=name[1]), 
                                Q(lastname__exact=name[0]))

        user.trainee.badge = b


        return HttpResponseRedirect(reverse('badges:index'))
        

    return render_to_response('badges/batch.html', context_instance=RequestContext(request))
