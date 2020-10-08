from django.urls import path, include

from .api import (
    VolumesList,
    MaterialsList,
    ProductsList,
    BrandsList,
    RadiusesList,
    OpticalPowersList,
    SubCategoriesList,
    ProductDetail,
)



urlpatterns = [
    path('list/', ProductsList.as_view()),
    path('detail/<int:pk>/', ProductDetail.as_view()),
    path('subcategories/', SubCategoriesList.as_view()),


    # FILTER
    path('volumes/', VolumesList.as_view()),
    path('materials/', MaterialsList.as_view()),
    path('brands/', BrandsList.as_view()),
    path('radiuses/', RadiusesList.as_view()),
    path('opt_powers/', OpticalPowersList.as_view()),

]