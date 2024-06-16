from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cars.models import Car
from dealers.models import Dealer
from wishlist.models import Wishlist
from .forms import CarSearchForm, ReviewForm


def home(request):
    return render(request, 'home.html')


def showroom(request):
    form = CarSearchForm(request.GET)
    cars = Car.objects.all()
    if form.is_valid():
        if form.cleaned_data['brand']:
            cars = cars.filter(brand=form.cleaned_data['brand'])
        if form.cleaned_data['min_price']:
            cars = cars.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            cars = cars.filter(price__lte=form.cleaned_data['max_price'])
    return render(request, 'showroom.html', {'form': form, 'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.car = car
            review.customer = request.user
            review.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = ReviewForm()
    return render(request, 'car_detail.html', {'car': car, 'form': form})


def dealers(request):
    _dealers = Dealer.objects.all()
    return render(request, 'dealers.html', {'dealers': _dealers})


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'dealer_detail.html', {'dealer': dealer})


@login_required(login_url='/login/')
def wishlist(request):
    _wishlist = Wishlist.objects.filter(customer=request.user)
    return render(request, 'wishlist.html', {'wishlist': _wishlist})


def login_view(request):
    return render(request, 'login.html')
