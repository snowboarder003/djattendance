#from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView, CreateView, DeleteView
#from .models import accounts
from accounts.models import User, ProfileForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from accounts.forms import UserForm

def add_profile(request):
        context = RequestContext(request)
        if request.method == 'POST':
                form = ProfileForm(request.POST)
                if form.is_valid():
                        user = form.save(commit=True)
                        # show the index page with the list of categories
                        return index(request)
                else:
                        # the form contains errors,
                        # show the form again, with error messages
                        pass
        else:
                # a GET request was made, so we simply show a blank/empty form.
                form = ProfileForm()

        # pass on the context, and the form data.
        return render_to_response('addprofile.html',
                {'form': form }, context)


"""
class HomeView(ListView):
    template_name = "profile/modprofile.html"
    model = User
    context_object_name = 'modprofile'

def modifyProfile(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        userform = UserForm(data=request.POST)
        
        # If the two forms are valid...
        if userform.is_valid():
            # Save the user's form data to the database.
            user = userform.save()

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print userform.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        userform = UserForm()

    # Render the template depending on the context.
    return render_to_response('modprofile.html',{'userform': userform}, context)

def index(request):
	return HttpResponse("Hello, world. You're at the polls index")
	##loginUser = APUserManager.create_user('lifeunion@gmail.com', '123456')

##@login_required
def view_profile(request, key):
	profile = User.get(key)
	payload = dict(profile = profile)
	return render_to_response ('profile.html', payload)
"""




