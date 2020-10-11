from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dashboard.urls')),
    path('', include('filters.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include([
        path('events/', include('events.urls')),
        path('products/', include('products.urls')),
        path('carts/', include('carts.urls')),
    ])),
    path('', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
