from django.forms.widgets import DateInput

class DatepickerWidget(DateInput):
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
