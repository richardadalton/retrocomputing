from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey('auth.User', blank=False, related_name="reviews_written")   
    product = models.ForeignKey(Product, blank=False, related_name="reviews_received")
    content = models.TextField()
    rating = models.IntegerField(blank=False, default=1)
    
    @property
    def stars(self):
        return range(self.rating)
    
    def __str__(self):
        return self.content
    
