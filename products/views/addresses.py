from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models.addresses import Address
from ..forms.addresses import AddressForm


class AddressListView(ListView):
    model = Address
    template_name = 'reads/address.html'
    context_object_name = 'address'


class AddressDetail(DetailView):
    model = Address
    template_name = 'details/address.html'
    context_object_name = 'address'
    pk_url_kwarg = 'pk'


class AddressCreate(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'creates/address.html'
    success_url = reverse_lazy('products:base')

    def form_valid(self, form):
        form.instance.saller = self.request.user
        return super().form_valid(form)


class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'updates/address.html'
    success_url = reverse_lazy('products:base')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:base', kwargs={'pk': self.object.pk})


class AddressDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('products:base')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

