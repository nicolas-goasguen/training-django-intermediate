from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Informations à venir.</p>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Site créé par Nicolas GOASGUEN.</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Informations à venir.</p>')
