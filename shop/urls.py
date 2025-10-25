from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

def home(request):

    return HttpResponseRedirect('/products/products/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', home),  
]