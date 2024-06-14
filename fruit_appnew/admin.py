from django.contrib import admin
from .models import Contact, categories, sub_category, prdct, Order
# Register your models here.
admin.site.register(Contact)
admin.site.register(categories)
admin.site.register(sub_category)
admin.site.register(prdct)
# admin.site.register(our_organic_products)
admin.site.register(Order)
