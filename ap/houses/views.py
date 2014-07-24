from django.views.generic.list import ListView
from .models import House

class HouseListView(ListView):
	model = House
	context_object_name = 'houses'
