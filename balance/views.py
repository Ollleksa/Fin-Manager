from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Balance
from django.template import loader

def index(request):
    money_list = Balance.objects.all()
    template = loader.get_template('home.html')
    context = {
        'money_list': money_list
    }
    #output = 'AAAAAAAAAAAA:   ' + str(money_list[0])
    #return HttpResponse(TemplateView.as_view(template_name='home.html'))
    return HttpResponse(template.render(context,request))
