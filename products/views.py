from django.shortcuts import render

# Create your views here.

def home(requests):
    context = {
        'product_entries': [
            {
                'title': 'Roses',
                'body': 'New breed with excellent color!',
            },
            {
                'title': 'Black Roses',
                'body': 'Magic black color!',
            },
            {
                'title': 'Daisy',
                'body': 'Rustic beauty!',
            }
        ]
    }
    return render(requests, "home.html", context)

def products(requests):
    return render(requests, "products.html")