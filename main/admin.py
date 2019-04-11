from django.contrib import admin
from .models import Restaurant, Food, complaint, Order,Order_content

# Register your models here.

class Food_Admin(admin.ModelAdmin):
	list_display=('Food_name','Food_price', 'Restaurant_items')
	search_fields = ('Food_name', 'Food_price')

class Restaurant_Admin(admin.ModelAdmin):
	list_display=('Restaurant_Name','Restaurant_email')
	search_fields=('Restaurant_Name',)

class Order_Admin(admin.ModelAdmin):
	list_display=('Orders_id','Restaurant_Order','phone_no','Address','Orders_total')
	search_fields=('Restaurant_Order','Orders_id')

class Order_content_Admin(admin.ModelAdmin):
	list_display=('Food_name',"Food_ID",'Food_quantity','Food_from')
	search_fields=('Food_name',)

admin.site.register(Food, Food_Admin)
admin.site.register(Restaurant,Restaurant_Admin)
admin.site.register(complaint)
admin.site.register(Order,Order_Admin)
admin.site.register(Order_content,Order_content_Admin)
