from django.forms import DateInput, TextInput, Select

class DatePickerInput(TextInput):
    class Media:
        js = ('datepicker.js' , )
        
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'datepicker'}
        super(DatePickerInput, self).__init__(*args, **kwargs)
        

class Select2Input(Select):
    class Media:
        js = ('select2.min.js', 'select2.js', )
        css = {
            'all': ('select2.min.css', )
        }
        
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'select2'}
        super(Select2Input, self).__init__(*args, **kwargs)   