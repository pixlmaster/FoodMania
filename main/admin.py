from django.contrib import admin
from .models import Restaurant, Food, complaint, Order,Order_content

# Register your models here.

admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(complaint)
admin.site.register(Order)
admin.site.register(Order_content)
