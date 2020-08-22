# Generated by Django 3.0.5 on 2020-07-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0014_auto_20200720_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='tours',
            name='content_kk',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='tours',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='tours',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tours',
            name='title_kk',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tours',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
