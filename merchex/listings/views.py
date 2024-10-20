from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from listings.forms import ContactUsForm
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def listing_list(request):
    listings_ = Listing.objects.all()
    return render(request, 'listings/listing_list.html',
                  {'listings': listings_})

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

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
