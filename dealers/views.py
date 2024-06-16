from django.shortcuts import render, get_object_or_404
from .models import Dealer

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'dealers/dealer_list.html', {'dealers': dealers})

def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'dealers/dealer_detail.html', {'dealer': dealer})

