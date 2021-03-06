# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-11 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('iRank', models.IntegerField()),
                ('wRank', models.IntegerField()),
                ('description', models.TextField()),
                ('website', models.CharField(max_length=500)),
                ('acronym', models.CharField(max_length=50)),
                ('founded', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'universities',
            },
        ),
    ]
