from django.shortcuts import render
from django.http import HttpResponse
from pw.models import Products

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    context = {
        'products': products
    }

    return render(request, 'pw/index.html', context)


def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'pw/product_detail.html', context)


