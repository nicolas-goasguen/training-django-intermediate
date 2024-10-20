from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from listings.forms import BandForm, ContactUsForm, ListingForm
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method == 'POST':
        band_form = BandForm(request.POST)
        if band_form.is_valid():
            band = band_form.save()
            return redirect('band-detail', band.id)
    else:
        band_form = BandForm()
    return render(request, 'listings/band_create.html', {'form': band_form})

def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band_form = BandForm(request.POST, instance=band) # instance is mandatory
        if band_form.is_valid():
            band_form.save()
            return redirect('band-detail', band.id)
    else:
        band_form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': band_form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})

def listing_list(request):
    listings_ = Listing.objects.all()
    return render(request, 'listings/listing_list.html',
                  {'listings': listings_})

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        listing_form = ListingForm(request.POST)
        if listing_form.is_valid():
            listing = listing_form.save()
            return redirect('listing-detail', listing.id)
    else:
        listing_form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': listing_form})

def listing_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, instance=listing)
        if listing_form.is_valid():
            listing_form.save()
            return redirect('listing-detail', listing.id)
    else:
        listing_form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': listing_form})

def listing_delete(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request, 'listings/listing_delete.html')

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            send_mail(
                subject=f'Message from {contact_form.cleaned_data["name"] 
                    or "Nicolas"} via MerchEx Contact Us form',
                message=contact_form.cleaned_data['message'],
                from_email=contact_form.cleaned_data['email'],
                recipient_list=['alias.goasguen@icloud.com'],
            )
            return redirect('email-sent')
    else:
        contact_form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': contact_form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')
