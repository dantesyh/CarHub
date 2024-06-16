from django.conf import settings
from django.db import models


class Car(models.Model):
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ServiceAppointment(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 3},
                                 related_name='appointments')
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, related_name='appointments')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    service_type = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 3})
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)
