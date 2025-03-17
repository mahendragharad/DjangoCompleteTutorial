
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item 
from django.template import loader 


def detail(request,item_id) : 
    item = Item.objects.get(pk=item_id) 
    context = {
        'item' : item ,
    }
    return render(request, 'Foodie/detail.html', context)

def index(request):
    Items_list = Item.objects.all() 
    template = loader.get_template('Foodie/index.html') 
    context = {
        'Items_list' : Items_list,
    }

    return HttpResponse(template.render(context, request))

def render2(request) : 
    Items_list = Item.objects.all()
    context = {
        "Items_list" : Items_list ,
    }

    return render(request, 'Foodies/index.html', context)

def items(request) :
    Items_list = Item.objects.all() 
    return HttpResponse(Items_list)




