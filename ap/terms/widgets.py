from django.forms.widgets import DateInput
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe

class DatepickerWidget(DateInput):
    format = '%m/%d/%Y'
    
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'datepicker'}
        super(DatepickerWidget, self).__init__(*args, **kwargs)
        
    class Media:
        css = {
            'all': ('jquery/css/jquery-ui-1.10.3.min.css',
                    'jquery/css/datepicker.css',)
        }
        js = (
            'jquery/js/jquery-1.10.1.min.js',
            'jquery/js/jquery.ui.core.js',
            'jquery/js/jquery.ui.datepicker.js',
            'js/datepicker.js',
        )

class CustomRadioSelect(RadioSelect):
    # make css file to remove bullets. or make no-bullets renderer.
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'radioselect'}
        super(CustomRadioSelect, self).__init__(*args, **kwargs)
    
    class Media:
        css = {
            'all': ('css/radioselect.css',)
        }

class HorizRadioRenderer(RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
