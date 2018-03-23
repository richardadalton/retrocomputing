from django.db import models
from django.db.models import Avg

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    @property
    def average_rating(self):
        average = self.reviews_received.all().aggregate(Avg('rating'))
        return average['rating__avg']

    @property
    def stars(self):
        return range(int(self.average_rating))

    def __str__(self):
        return self.name