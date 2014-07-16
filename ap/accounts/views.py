from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, UpdateView

from accounts.models import User
from accounts.forms import UserForm, EmailForm


class EmailUpdateView(UpdateView):
    model = User
    form_class = EmailForm
    template_name = 'accounts/email_change.html'

    def get_success_url(self):
        messages.success(self.request, "Email Updated Successfully!")
        return reverse_lazy('user-detail', kwargs={'pk': self.kwargs['pk']})


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/update_user.html'

    def get_success_url(self):
        messages.success(self.request,
                         "User Information Updated Successfully!")
        return reverse_lazy('user-detail', kwargs={'pk': self.kwargs['pk']})


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'accounts/user_detail.html'
