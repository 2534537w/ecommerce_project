# Generated by Django 2.2.17 on 2021-03-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
