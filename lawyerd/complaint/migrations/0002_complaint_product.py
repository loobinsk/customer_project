# Generated by Django 2.2.3 on 2019-11-07 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('complaint', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='product',
            field=models.ForeignKey(help_text='Product', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]