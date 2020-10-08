from django.urls import path

from .views import  (
    dashboard,
    products,
    glasses,

    GlassesDetailView
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('products/glasses/', glasses, name='glasses'),
    path('products/glasses/detail/<int:pk>/', GlassesDetailView.as_view(), name='glasses_detail'),
]