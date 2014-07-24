from django.views.generic.list import ListView
from .models import House, Bunk

class HouseListView(ListView):
	model = House
	context_object_name = 'houses'
	template_name = 'houses/house_list.html'


class BunkListView(ListView):
	model = Bunk
	context_object_name = 'bunks'
	template_name = 'houses/bunk_list.html'
