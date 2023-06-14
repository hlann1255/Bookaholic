
from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True) 
    Author= models.CharField(max_length=50, blank=True)
    Publishing= models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=0)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField() 
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True) 
    modified_date = models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('book_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.product_name 

