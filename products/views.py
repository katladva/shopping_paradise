from django.shortcuts import render
from django.urls import reverse_lazy
from products.models import Product
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
import pdb

# Create your views here.

def home(requests):
    recent_products = Product.objects.all()
    return render(requests, "home.html", {'products': recent_products})


@login_required
def products(request):
    #pdb.set_trace()
    p = Product.objects.filter(author=request.user)
    return render(request, 'products.html', {'products': p})


class ProductCreateView(CreateView):
    model = Product
    template_name = 'new_product.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)