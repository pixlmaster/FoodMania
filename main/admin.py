from django.contrib import admin
from .models import Restaurant, Food, Menu

# Register your models here.

admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Restaurant)
