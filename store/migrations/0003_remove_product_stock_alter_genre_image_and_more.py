# Generated by Django 4.1.3 on 2022-12-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_author_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/genre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/product'),
        ),
    ]