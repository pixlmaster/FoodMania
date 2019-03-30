from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Restaurant_Name = models.CharField(max_length=200, default="Restaurant")
    Restaurant_email = models.CharField(max_length=200, default="null"	)
    Restaurant_Description = models.CharField(max_length=200, default="none")
    Restaurant_image = models.ImageField(upload_to="images/", default="no image")

    def __str__(self):
        return self.Restaurant_Name

    