from django.urls import path, include

urlpatterns = [
    path('user/', include('user.api.v1.urls')),
    path('cart/', include('cart.api.v1.urls')),
    path('heart/', include('heart.api.v1.urls')),
    path('order/', include('order.api.v1.urls')),
    path('product/', include('product.api.v1.urls')),
]
