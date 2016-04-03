from django.forms import ModelForm
from django import forms

from demo.models import Demo, CHAR_CHOICES
from demo.widget import DatePickerInput, Select2Input


class DemoForm(ModelForm):
    date = forms.DateField(widget=DatePickerInput)
    char = forms.ChoiceField(choices=CHAR_CHOICES, widget=Select2Input)
    
    class Meta:
        model = Demo
        fields = ('date', 'char', )