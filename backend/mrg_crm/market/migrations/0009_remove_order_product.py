# Generated by Django 3.2.8 on 2022-04-04 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
