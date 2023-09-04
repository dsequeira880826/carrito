from django.shortcuts import render
from django.views.generic import TemplateView

class saludo(TemplateView):
    template_name= 'saludo.html'