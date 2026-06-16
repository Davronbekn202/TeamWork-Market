from django.contrib import admin
from .models.products import Product, ProductImage
from .models.categories import Category
from .models.addresses import Address
from .models.banners import Banner
from .models.brands import Brand
from .models.cart import Cart, CartItem
from .models.colors import Color, ProductColor
from .models.coupons import Coupon
from .models.newsletter import Subscriber
from .models.orders import Order, OrderItem
from .models.payments import Payment
from .models.reviews import Review
from .models.sizes import Size, ProductSize
from .models.wishlist import Wishlist

admin.site.register(Product)
admin.site.register(ProductImage)

admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Banner)
admin.site.register(Brand)

admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(Review)
admin.site.register(Subscriber)
admin.site.register(Payment)
admin.site.register(Wishlist)
admin.site.register(Coupon)

admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Size)
admin.site.register(ProductSize)
