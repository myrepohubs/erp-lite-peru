from django.shortcuts import render

# Create your views here.

# core/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'