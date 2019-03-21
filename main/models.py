from django.db import models

# Create your models here.
class foodmania(models.Model):
    user_Name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)

    def __str__(self):
        return self.user_Name