from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #mus = {'no_of_slides': nSlides,'range':range(1,nSlides),'product': products}
    #allProds = [[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]

    allProds = []
    catprods = Product.objects.values('subcategory','id')
    cats = {item['subcategory'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(subcategory=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides]) 
    mus = {'allProds':allProds}
    return render(request,'shop/index.html',mus)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def pView(request):
    return render(request,'shop/pView.html')

def checkout(request):
    return render(request,'shop/checkout.html')

