# Generated by Django 4.0.4 on 2022-06-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_category_alter_product_image_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(to='ecommerce.product'),
        ),
    ]
