from django.views.generic import TemplateView, DetailView

from .models import Template, Chart


class TemplateCreate(TemplateView):
    template_name = "seating/template_create.html"


class TemplateDetail(DetailView):
    queryset = Template.objects.all()
    template_name = "seating/template_detail.html"
