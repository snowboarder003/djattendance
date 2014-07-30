from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Bunk
from .forms import BunkForm


class BunkListView(ListView):
	model = Bunk
	context_object_name = 'bunks'
	template_name = 'houses/bunk_list.html'


class BunkFormView(FormView):
	form_class = BunkForm
	template_name = 'houses/bunk_update.html'