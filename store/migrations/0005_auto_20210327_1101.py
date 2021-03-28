# Generated by Django 2.2.17 on 2021-03-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]