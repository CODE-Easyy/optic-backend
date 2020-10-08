from django.urls import path, include

from .api import (
    VolumesList,
    MaterialsList,
    ProductsList,
    BrandsList,
    RadiusesList,
    OpticalPowersList
)



urlpatterns = [
    path('list/', ProductsList.as_view()),


    # FILTER
    path('volumes/', VolumesList.as_view()),
    path('materials/', MaterialsList.as_view()),
    path('brands/', BrandsList.as_view()),
    path('radiuses/', RadiusesList.as_view()),
    path('opt_powers/', OpticalPowersList.as_view()),

]