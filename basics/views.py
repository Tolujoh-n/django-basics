from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import basics
from django.urls import reverse

# Create your views here.

def index(request):
    basicsnames = basics.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'basicsnames': basicsnames,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = basics(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = basics.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    member = basics.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = basics.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))





def testing(request):
    template = loader.get_template('tags.html')
    context = {
        'greeting': 1,
        'firstname': 'Tolu john',
        'day': 'friday',
        'fruits': ['apple', 'banana', 'cherry'],
        'x': ['mango', 'orange', 'pawpaw'],
        'y': ['mango', 'orange', 'pawpaw'],
    }
    return HttpResponse(template.render(context, request))















