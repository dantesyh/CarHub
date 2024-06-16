from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showroom/', views.showroom, name='showroom'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('dealers/', views.dealers, name='dealers'),
    path('dealer/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('login/', views.login_view, name='login'),
]
