from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include("cart.urls", namespace="cart")),
    path('orders/', include("orders.urls", namespace="orders")),
    path('', include("shop.urls", namespace="shop")),
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
            )
