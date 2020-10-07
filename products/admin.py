from django.contrib import admin

from .models import *


admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Volume)
admin.site.register(OpticalPower)
admin.site.register(Radius)
admin.site.register(Brand)
admin.site.register(Material)

