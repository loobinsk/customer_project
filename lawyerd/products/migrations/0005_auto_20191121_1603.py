# Generated by Django 2.2.7 on 2019-11-21 14:03

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191120_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='document',
            field=models.FileField(null=True, upload_to=products.models.product_get_file_path, validators=[products.models.validate_product_file_extension], verbose_name='Proof of product rights (Trademark from Global Brand Database or national registers)'),
        ),
    ]
