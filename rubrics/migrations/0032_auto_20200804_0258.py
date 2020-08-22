# Generated by Django 3.0.5 on 2020-08-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0031_auto_20200804_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourists',
            name='short_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='tourists',
            name='short_description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='tourists',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='tours',
            name='short_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='tours',
            name='short_description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='tours',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
    ]
