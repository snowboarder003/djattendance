from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from buglog.models import BugForm, Bug
from django.views import generic

class BuglogListView(generic.ListView):
    model = Bug
    template_name = 'buglog/list.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        return Bug.objects.all

class BuglogView(generic.FormView):
    template_name = 'buglog/log.html'
    form_class = BugForm
    success_url = '/buglog/thanks/'
    
    def form_valid(self, form):
        if self.request.method == 'POST':
            form = BugForm(self.request.POST)
            if form.is_valid():
                new_bug = form.save()
                new_bug.firstname = self.request.user.firstname
                new_bug.lastname = self.request.user.lastname
                new_bug.save()
                # new_bug.create_issue()
        return super(BuglogView, self).form_valid(form)

class BugThanksView(generic.TemplateView):
    template_name = 'buglog/thanks.html'