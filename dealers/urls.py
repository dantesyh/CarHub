from django.urls import path
from . import views

urlpatterns = [
    path('', views.dealer_list, name='dealer_list'),
    path('<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
]
