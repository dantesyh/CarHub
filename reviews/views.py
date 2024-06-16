from django.shortcuts import redirect
from .models import Review
from cars.forms import ReviewForm

def add_review(request, car_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.car_id = car_id
            review.customer = request.user
            review.save()
            return redirect('car_detail', car_id=car_id)
    return redirect('showroom')

