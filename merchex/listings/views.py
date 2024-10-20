from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def listings(request):
    listings_ = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings_})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')
