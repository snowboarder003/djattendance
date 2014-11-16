from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Bunk, House
from .forms import BunkForm
from accounts.models import Trainee


"""Phil 3:20 'Our commonwealth exists in the heavens, from which also 
we eagerly await a Savior, the Lord Jesus Christ' """

class BunkListView(ListView):
	model = House
	context_object_name = 'houses'
	template_name = 'houses/bunk_list.html'

	def get_context_data(self, **kwargs):
		context = super(BunkListView, self).get_context_data(**kwargs)
		context['trainees'] = Trainee.objects.all()
		return context

	def post(self, request, *args, **kwargs):
		for value in request.POST.getlist('select-trainee'):
			bunk = Bunk.objects.get(pk=int(value.split('-')[0]))
			trainee = Trainee.objects.get(pk=int(value.split('-')[1]))
			trainee.bunk = None
			print trainee
			print trainee.bunk
			bunk.trainee = trainee
			trainee.save()
		return self.get(request, *args, **kwargs)

class TraineeListView(ListView):
	model = Trainee
	context_object_name = 'trainees'
	template_name = 'houses/trainee_list.html'


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
			bunk = Bunk.objects.get(pk=self.kwargs['pk'])
			new_occupant = form.cleaned_data['trainee']

			# if bunk were to be assigned to 'vacant'
			if new_occupant == None:
				if hasattr(bunk, 'trainee'):
					old_occupant = bunk.trainee
					old_occupant.bunk = None
					old_occupant.save()
			# if bunk is vacant	
			elif not hasattr(bunk, 'trainee'):
				new_occupant.bunk = bunk
				new_occupant.save()
			# if new_occupant is to replace the old occupant
			elif hasattr(bunk, 'trainee') and new_occupant.bunk == None:
				old_occupant = bunk.trainee
				old_occupant.bunk = None
				new_occupant.bunk = bunk
				old_occupant.save()
				new_occupant.save()
			# if new_occupant were to swap with old occupant
			elif hasattr(bunk, 'trainee') and new_occupant.bunk != None:
				old_occupant = bunk.trainee
				old_occupant.bunk = new_occupant.bunk
				new_occupant.bunk = bunk
				old_occupant.save()
				new_occupant.save()

		return super(BunkFormView, self).form_valid(form)
