from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
def home(request):
    products= Product.objects.all().filter(is_available=True)   #https://docs.djangoproject.com/en/3.2/topics/db/managers/
 
    context = {
        'products': products,
    }
    return render(request,'home.html',context)

def policy(request):
    return render(request, 'includes/policy.html')