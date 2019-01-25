from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Balance, Money_item
from django.template import loader
from .forms import Update_Balance

def update_bal(request):
    if request.method == 'POST':
        form = Update_Balance(request.POST)
        if form.is_valid():
            b = Balance.objects.get(id=1)
            b.balance_count = form.cleaned_data['new_balance']
            b.save()

    else:
        form = Update_Balance()

    money_list = Balance.objects.all()
    template = loader.get_template('current_balance.html')
    context = {
        'money_list': money_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def log_creation(request):
    log_list = Money_item.objects.all()
    template = loader.get_template('log_page.html')
    context = {
        'log_list': log_list,
    }
    return HttpResponse(template.render(context, request))