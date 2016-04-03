from django.shortcuts import render
from django.views.generic import CreateView, ListView

from demo.models import Demo
from demo.forms import DemoForm

class DemoCreateView(CreateView):
    model = Demo
    form_class = DemoForm

    
class DemoListView(ListView):
    model = Demo
