from django.core.urlresolvers import reverse_lazy
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
	success_url = reverse_lazy('houses:bunk_list')

	def get_context_data(self, **kwargs):
		context = super(BunkFormView, self).get_context_data(**kwargs)
		context['bunk'] = Bunk.objects.get(pk=self.kwargs['pk'])
		return context

	def form_valid(self, form):
		if form.is_valid():
			if form.cleaned_data['trainee'] == None:
				Bunk.objects.get(pk=self.kwargs['pk']).trainee.bunk = None
			else:
				trainee = form.cleaned_data['trainee']
				trainee.bunk = Bunk.objects.get(pk=self.kwargs['pk'])
				trainee.save()
		return super(BunkFormView, self).form_valid(form)