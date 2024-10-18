from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Informations à venir.</p>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Site créé par Nicolas GOASGUEN.</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Informations à venir.</p>')
