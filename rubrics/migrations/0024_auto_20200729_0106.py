# Generated by Django 3.0.5 on 2020-07-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0023_auto_20200728_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='gallery_pages', verbose_name='Галлерея фото'),
        ),
        migrations.AlterField(
            model_name='tourists',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='thumbnail_tourists', verbose_name='Главное фото'),
        ),
    ]
