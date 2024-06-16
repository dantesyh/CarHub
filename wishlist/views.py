from django.shortcuts import render, redirect

from .models import Wishlist


def view_wishlist(request):
    wishlist = Wishlist.objects.filter(customer=request.user)
    return render(request, 'view_wishlist.html', {'wishlist': wishlist})


def add_to_wishlist(request, car_id):
    if request.method == 'POST':
        wishlist_item, created = Wishlist.objects.get_or_create(customer=request.user, car_id=car_id)
        if created:
            wishlist_item.save()
    return redirect('car_detail', car_id=car_id)
