from django.db import models
from django.conf import settings

class Dealer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    dealership_name = models.CharField(max_length=255)
    contact_info = models.TextField()
    profile_picture = models.ImageField(upload_to='dealer_profiles/', blank=True, null=True)

