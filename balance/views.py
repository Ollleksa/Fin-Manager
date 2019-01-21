from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Balance

def index(request):
    #return HttpResponse(TemplateView.as_view(template_name='home.html'))
    pass
