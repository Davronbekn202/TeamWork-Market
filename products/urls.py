from django.urls import path
from .views import product, addresses

app_name = "products"

urlpatterns = [
    # product & product-images

    path('', product.ProductListView.as_view(), name='base'),
    path('create-product/', product.ProductCreate.as_view(), name='create-product'),
    path('update-product/<int:pk>/', product.ProductUpdate.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', product.ProductDelete.as_view(), name='delete-product'),
    path('detail-product/<int:pk>/', product.ProductDetail.as_view(), name='delete-product'),

    path('image-product-create/<int:pk>/', product.ProductImageCreate.as_view(), name='image-product-create'),
    path('image-product-update/<int:pk>/', product.ProductImageUpdate.as_view(), name='image-product-update'),
    # Address

    path('address/', addresses.AddressListView.as_view(), name='address'),
    path('address-detail/<int:pk>/', addresses.AddressDetail.as_view(), name='address-detail'),
    path('address-create/<int:pk>/', addresses.AddressCreate.as_view(), name='address-create'),
    path('address-update/<int:pk>/', addresses.AddressUpdate.as_view(), name='address-update'),
    path('address-delete/<int:pk>/', addresses.AddressDelete.as_view(), name='address-delete'),

]
