from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from shop.models import Goods


def product_list(request):
    products = Goods.objects.all()
    return render(request, 'shop/product_list.html', context={'products': products})


def product_detail(request, id):
    product = get_object_or_404(Goods, id=id)
    return render(request, 'shop/product_detail.html', context={'product': product})
