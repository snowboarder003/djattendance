# Create your views here.
from django.views.generic import CreateView, DetailView
from braces.views import LoginRequiredMixin

from .models import Portion
from .forms import CreateForm

class CreatePortion(LoginRequiredMixin, CreateView):
    form_class = CreateForm
    model = Portion
    context_object_name = 'portion'
    
    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super(CreatePortion, self).form_valid(form)

class DetailPortion(LoginRequiredMixin, DetailView):
    model = Portion
    context_object_name = 'portion'