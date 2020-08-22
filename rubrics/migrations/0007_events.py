# Generated by Django 3.0.5 on 2020-07-19 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0006_auto_20200719_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='thumbnail_events', verbose_name='Главное фото')),
                ('content', models.TextField(verbose_name='Контент')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
