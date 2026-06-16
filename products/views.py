from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView
from .models.products import Product


class ProductListView(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'car'
