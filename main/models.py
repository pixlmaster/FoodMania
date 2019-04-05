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
	Food_name = models.CharField(max_length=200, default="none");
	Food_price = models.IntegerField()
	Restaurant_items = models.ForeignKey(Restaurant, default=1, verbose_name="Restaurants", on_delete=models.SET_DEFAULT)
	Food_slug = models.CharField(max_length=200, default=1)
	def __str__(self):
		return self.Food_name


class complaint(models.Model):
    Username= models.CharField(max_length=200, default="none")
    Message = models.CharField(max_length=200, default="none")


    def __str__(self):
        return self.Username


def create(name, message):
    comp=complaint()
    comp.Username=name
    comp.Message=message
    return comp    