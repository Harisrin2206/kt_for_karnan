from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import userdata

def user(request):
    user= userdata.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'userdata':user,
    }

    return HttpResponse(template.render(context,request))

def portfolio(request,id):
    a= userdata.objects.all().get(id=id)
    template = loader.get_template('portfolio.html')
    context = {
        'userdata':a,
    }

    return HttpResponse(template.render(context,request))