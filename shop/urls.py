from django.contrib import admin
from django.urls import path, include  
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Shop API is working!'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  
    path('', home),
]