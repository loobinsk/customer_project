# Generated by Django 2.2.7 on 2021-03-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0011_auto_20210224_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='search_text',
            field=models.CharField(default='', help_text='Search text', max_length=1000),
        ),
    ]
