from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirect root URL "/" → "/products/"
    path('', lambda request: redirect('products')),  
    
    path('', include('myapp.urls')),  
]
