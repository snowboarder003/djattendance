from django.views.generic.list import ListView
from .models import Bunk


class BunkListView(ListView):
	model = Bunk
	context_object_name = 'bunks'
	template_name = 'houses/bunk_list.html'
