from django.views.generic import TemplateView

from .models import Template, Chart


class TemplateCreate(TemplateView):
    template_name = "seating/template_create.html" 
