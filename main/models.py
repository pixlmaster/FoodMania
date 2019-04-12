from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Restaurant_Name = models.CharField(max_length=200, default="Restaurant")
    Restaurant_email = models.CharField(max_length=200, default="null"	)
    Restaurant_Description = models.CharField(max_length=200, default="none")
    Restaurant_image = models.ImageField(upload_to="images/", default="no image")
    Restaurant_slug = models.CharField(max_length=200, default=1)
 
    class Meta:
        verbose_name_plural = "Restaurants"   

    def __str__(self):
        return self.Restaurant_Name



class Food(models.Model):
    Food_name = models.CharField(max_length=200, default="none")
    Food_price = models.IntegerField()
    Restaurant_items = models.ForeignKey(Restaurant, default=1, verbose_name="Restaurants", on_delete=models.CASCADE)
    Food_slug = models.CharField(max_length=200, default=1)
    ordering = ['Restaurant_items']
    def __str__(self):
        return self.Restaurant_items.Restaurant_Name+"-"+self.Food_name


class complaint(models.Model):
    Username= models.CharField(max_length=200, default="none")
    Message = models.TextField(max_length=200, default="none")


    def __str__(self):
        return self.Username


def create(name, message):
    comp=complaint()
    comp.Username=name
    comp.Message=message
    return comp    

class Order(models.Model):
    Orders_id = models.CharField(max_length=200, default="0")
    Orders_total = models.IntegerField(default=0) 
    Restaurant_Order= models.CharField(max_length=200, default="0")
    phone_no = models.CharField(max_length=200, default="not given")
    Address = models.CharField(max_length=200, default="not given")
    ordering = ['Restaurant_Order']
    class Meta:
        verbose_name_plural = "Orders"   

    def __str__(self):
        return self.Restaurant_Order

def create_Order(ID, total, rest_name, Address, Phone):
    order=Order()
    order.Orders_id=str(ID)
    order.Orders_total=total
    order.Restaurant_Order= rest_name
    order.Address=Address
    order.phone_no=Phone
    return order

class Order_content(models.Model):
    Food_name = models.CharField(max_length=200, default="none");
    Food_quantity = models.IntegerField(default=0)
    Food_ID = models.CharField(max_length=200, default="none")
    Food_from = models.ForeignKey(Order, default=1, verbose_name="Orders", on_delete=models.CASCADE)
    ordering = ['Food_from']
    def __str__(self):
        return (self.Food_name +"-"+ self.Food_from.Orders_id)

def create_Order_cont(name, quant, ID, orderID):
    container=Order_content()
    container.Food_name=name
    container.Food_quantity=quant
    container.Food_from = ID
    container.Food_ID = orderID
    return container