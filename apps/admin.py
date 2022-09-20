from django.contrib import admin
from .models import Firma, Type, Product, Nakladnoy

admin.site.register(Firma)
admin.site.register(Type)
admin.site.register(Nakladnoy)
admin.site.register(Product)
