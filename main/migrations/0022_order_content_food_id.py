# Generated by Django 2.1.7 on 2019-04-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190411_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_content',
            name='Food_ID',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
