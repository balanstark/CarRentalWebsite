from django.contrib import admin
from carapp.models import Company,Product,ProductInteriorImgs,ProductExteriorImgs

# Register your models here.

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductInteriorImgs)
admin.site.register(ProductExteriorImgs)
