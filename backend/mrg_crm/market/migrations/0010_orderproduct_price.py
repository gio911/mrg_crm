# Generated by Django 3.2.8 on 2022-04-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_remove_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]