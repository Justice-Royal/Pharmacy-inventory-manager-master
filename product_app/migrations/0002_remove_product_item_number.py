# Generated by Django 3.0.8 on 2020-10-25 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='item_number',
        ),
    ]