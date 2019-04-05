from django.contrib import admin
from .models import Restaurant, Food, complaint

# Register your models here.

admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(complaint)
