from django.shortcuts import render
from django.views.generic import base
# Create your views here.

class HomePage(base.TemplateView):
    template_name = 'home.html'

