from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all() if hasattr(Product, 'objects') else []
    return JsonResponse({'message': 'Product list works!', 'count': len(products)})

def product_detail(request, id):
    return JsonResponse({'message': f'Product {id} detail works!'})