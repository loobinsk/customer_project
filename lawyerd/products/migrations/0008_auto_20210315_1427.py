# Generated by Django 2.2.19 on 2021-03-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210309_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='itype',
            field=models.IntegerField(choices=[(0, 'Game'), (1, 'Software'), (2, 'Photo'), (3, 'Picture'), (4, 'Course')], db_index=True, default=0, verbose_name='Type of product'),
        ),
    ]