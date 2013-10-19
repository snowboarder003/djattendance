# Create your views here.
from django.views.generic import CreateView, DetailView
from braces.views import LoginRequiredMixin

from .models import Portion

class CreatePortion(LoginRequiredMixin, CreateView):
    model = Portion
    context_object_name = 'portion'


class DetailPortion(LoginRequiredMixin, DetailView):
    model = Portion
    context_object_name = 'portion'