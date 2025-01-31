from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product, OrderItem
from django.db.models import Sum
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/product_list.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_products'] = Product.objects.count() 
        context['total_stock'] = Product.objects.aggregate(Sum('stock'))['stock__sum'] or 0
        context['total_sold'] = OrderItem.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0

        query = self.request.GET.get('q', '')
        if query:
            context['products'] = Product.objects.filter(ItemName__icontains=query)

        return context

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'app/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['ItemName', 'description', 'price', 'stock']
    template_name = 'app/product_create.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['ItemName', 'description', 'price', 'stock']
    template_name = 'app/product_update.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_delete.html'
    success_url = reverse_lazy('product')
