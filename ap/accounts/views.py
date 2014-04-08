#from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView, CreateView, DeleteView
#from .models import accounts
from accounts.models import User, EmailForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from accounts.forms import UserForm
from django.core.urlresolvers import reverse

def change_profile(request):
        context = RequestContext(request)
        if request.method == 'POST':
                form = EmailForm(request.POST, instance = request.user)
                if form.is_valid():
                        form.save(commit=True)
                        return HttpResponseRedirect(reverse('ap.views.home'))
                else:
                        # the form contains errors,
                        # show the form again, with error messages
                        pass
        else:
                # a GET request was made, so we simply show a blank/empty form.
                form = EmailForm()

        # pass on the context, and the form data.
        return render_to_response('changeprofile.html',
                {'form': form }, context)




