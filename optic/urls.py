from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/', include('filters.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include([
        path('events/', include('events.urls')),
        path('products/', include('products.urls')),
    ])),
    path('', include('orders.urls')),
    path('', include('contacts.urls')),


    path('', TemplateView.as_view(template_name='index.html')),
    path('cart', TemplateView.as_view(template_name='index.html')),
    path('aboutUs', TemplateView.as_view(template_name='index.html')),
    path('salon', TemplateView.as_view(template_name='index.html')),
    path('delivery', TemplateView.as_view(template_name='index.html')),
    path('product/<id>', TemplateView.as_view(template_name='index.html')),
    path('event/<id>', TemplateView.as_view(template_name='index.html')),
    path('cart/order', TemplateView.as_view(template_name='index.html')),
    path('product/<cat>/<subcat>', TemplateView.as_view(template_name='index.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
