from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from ..models.products import Product, ProductImage
from ..forms.product import ProductForm, ProductImageForm


class ProductListView(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = ProductImage
    template_name = 'details/products.html'
    context_object_name = 'products'
    pk_url_kwarg = 'pk'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "creates/products.html"
    success_url = reverse_lazy('products:image-product-create')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'updates/products.html'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:image-product-create', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:base')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProductImageCreate(CreateView):
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'creates/product_images.html'
    success_url = reverse_lazy('products:base')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductImageUpdate(UpdateView):
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'updates/product_images.html'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:base', kwargs={'pk': self.object.pk})
