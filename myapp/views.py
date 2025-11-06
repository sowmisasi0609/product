from django.shortcuts import render

def product_list(request):
    products = [
        {"name": "Smart Watch", "price": 2999, "image": "images/watch.jpeg", "category": "gadgets", "sale": True},
        {"name": "Wireless Earbuds", "price": 1999, "image": "images/earbuds.jpg", "category": "gadgets", "sale": False},
        {"name": "Men Casual Shirt", "price": 899, "image": "images/shirt.jpeg", "category": "clothing", "sale": True},
        {"name": "phone", "price": 14999, "image": "images/phone.jpg", "category": "gadgets", "sale": False},
    ]
    return render(request, "myapp/products.html", {"products": products})

