# Create your views here.
from django.views.generic import CreateView, DetailView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .models import Portion
from .forms import CreateForm


class TodaysPortion(LoginRequiredMixin, RedirectView):

    permanent = False
    query_string = False

    def get_redirect_url(self, pk=Portion.today().pk):
        return reverse_lazy('dailybread:detail', kwargs={'pk':pk})


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


