from rest_framework.routers import DefaultRouter

from .api import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('list', CartViewSet)
router.register('items', CartItemViewSet)


urlpatterns = [

] + router.urls