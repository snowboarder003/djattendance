from django.views.generic.edit import FormView
from .forms import NewAnnouncementForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class AnnouncementView(FormView):
	template_name = 'announcements/announcement_list.html'
	form_class = NewAnnouncementForm
	success_url = reverse_lazy('announcement_list')

	def get_context_data(self, **kwargs):
		context = super(AnnouncementView, self).get_context_data(**kwargs)
		return context
