# Generated by Django 3.2.9 on 2023-02-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_zip_code_shippingaddress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]