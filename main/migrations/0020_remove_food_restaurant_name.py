# Generated by Django 2.1.7 on 2019-04-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_food_restaurant_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Restaurant_Name',
        ),
    ]