from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories':Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def product(request):
    template = loader.get_template('product.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


