from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Voici quelques exemples d'annonces :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Site créé par Nicolas GOASGUEN.</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Informations à venir.</p>')
