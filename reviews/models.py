from django.db import models
from django.conf import settings
class Review(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 3})
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

