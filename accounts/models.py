from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Seller")
    
    def __str__(self):
        return self.user.username + ' Seller Account'

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Buyer")
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username  + ' Buyer Account'
