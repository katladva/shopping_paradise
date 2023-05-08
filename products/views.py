from django.shortcuts import render
from django.urls import reverse_lazy
from products.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
import pdb

# Create your views here.

def home(request):
    recent_products = Post.objects.all().order_by('-created_date')
    return render(request, "home.html", {'products': recent_products})


@login_required
def products(request):
    #pdb.set_trace()
    p = Post.objects.filter(author=request.user)
    return render(request, 'products.html', {'products': p})


class ProductCreateView(CreateView):
    model = Post
    template_name = 'new_product.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)