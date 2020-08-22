# Generated by Django 3.0.5 on 2020-07-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0022_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeseat',
            name='slug',
            field=models.SlugField(blank=True, max_length=70, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='typesstay',
            name='slug',
            field=models.SlugField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
